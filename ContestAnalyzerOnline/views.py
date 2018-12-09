from django.shortcuts import render, redirect
from string import ascii_uppercase
import itertools
from ContestAnalyzerOnline.forms import ContestForm
from pycontestanalyzer.contest import Contest
from pycontestanalyzer.utils.downloads.logs import get_list_of_logs
from pycontestanalyzer.utils.contest import retrieve_contest_object
from pycontestanalyzer.plot_dictionary import plot_dictionary

import logging
logging.basicConfig(format='%(levelname)s: %(asctime)s UTC  -  views.py : %(message)s', level=logging.DEBUG)

# Define output folder
output_folder = "./data/"


# ________________________________________________________________________________________________________
def index(request):
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            request.session['cleaned_data'] = form.cleaned_data
            if "new_callsign" in request.session.keys():
                del request.session['new_callsign']
            return render(request, 'processing.html', {'form': form})
    else:
        form = ContestForm()

    return render(request, 'index.html', {'form': form})


# ________________________________________________________________________________________________________
def process(request):
    # Get info from form
    search_info = request.session['cleaned_data']
    contest_type = search_info["name"]
    callsign = search_info["callsign"].upper()
    year = search_info["year"]
    mode = search_info["mode"]

    # Get call from availablecalls.html page. Store it in new_callsign so that it's available everywhere.
    if request.GET.get('call'):
        callsign = str(request.GET.get('call'))
        request.session['new_callsign'] = callsign

    # Download log and process it
    contest = Contest(
        contest=contest_type,
        year=year,
        mode=mode,
        callsign=callsign,
        output_folder=output_folder
    )

    # The call sign does not exist, provide list of available call signs
    if not contest.call_exists:
        list_of_calls = get_list_of_logs(contest_type=contest_type, year=year, mode=mode)
        list_of_calls.sort()
        calls_dict = {}
        for number in range(1,10):
            calls_dict[str(number)] = []
            for call in list_of_calls:
                if call[0] == str(number):
                    calls_dict[str(number)].append(call)
        for letter in ascii_uppercase:
            calls_dict[letter] = []
            for call in list_of_calls:
                if call[0] == letter:
                    calls_dict[letter].append(call)
        return render(request, 'analysis_availablecalls.html', {'contest': contest, 'callsDict':sorted(calls_dict.items())})

    # Check whether reverse beacon spots have been downloaded correctly
    if not contest.download_spots_ok:
        raise(NameError("Beacon spots not downloaded correctly"))

    # Loop over the tools if necessary
    logging.info("Process logs...")
    contest.process()
    logging.info("Logs processed")

    return redirect('contestAnalyzer:mainPage')


# ________________________________________________________________________________________________________
def main_page(request):
    # --- Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # --- Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)

    return render(request, 'analysis_main.html', {'contest': contest, 'nbar':'main'})


# ________________________________________________________________________________________________________
def contest_summary(request):
    # Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)

    summary_info = []
    summary_info_total = []

    qsos_cumul = 0
    dxcc_cumul = 0
    zones_cumul = 0
    points_cumul = 0
    for band in [10, 15, 20, 40, 80, 160]:
        qsos = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"] == band)]["call"].count()
        dxcc = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"] == band)]["dxcc"].value_counts().count()
        zones = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"] == band)]["mynr"].value_counts().count()
        points = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"] == band)]["points"].sum()
        qsos_cumul += qsos
        dxcc_cumul += dxcc
        zones_cumul += zones
        points_cumul += points
        if qsos>0:
            summary_info.append([
                band,
                qsos,
                dxcc,
                zones,
                points,
                float(points)/qsos,
                ])
        else:
            summary_info.append([
                band,
                qsos,
                dxcc,
                zones,
                points,
                0.,
                ])
    summary_info_total.append([
        "Total",
        qsos_cumul,
        dxcc_cumul,
        zones_cumul,
        points_cumul,
        float(points_cumul)/qsos_cumul,
        (zones_cumul+dxcc_cumul)*points_cumul
        ])

    return render(request, 'analysis_summary.html', {'summary_info': summary_info,
                                                     'summary_info_total': summary_info_total,
                                                     'nbar': 'summary'})


#________________________________________________________________________________________________________
def contest_log(request):
    # --- Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # --- Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)

    qsos_page = 50

    log = contest.log
    cumulated_info = []
    if request.GET.get('filter'):
        rule = str(request.GET['filter']).split(",")
        for r in rule:
            if "band" in r:
                band = int(r.replace("band:", ""))
                log = log[log["band"] == band]
                cumulated_info.append(r)
            if 'call' in r:
                call = str(r.replace("call:", ""))
                log = log[log["call"] == call]
                cumulated_info.append(r)
            if 'freq' in r:
                freq = float(r.replace("freq:", ""))
                log = log[log["frequency"] == freq]
                cumulated_info.append(r)
            if 'date' in r:
                date = str(r.replace("date:", ""))
                log = log[log["date"] == date]
                cumulated_info.append(r)
            if 'time' in r:
                time = str(r.replace("time:", ""))
                log = log[log["time"] == time]
                cumulated_info.append(r)
            if 'cont' in r:
                cont = str(r.replace("cont:", ""))
                log = log[log["continent"] == cont]
                cumulated_info.append(r)
            if 'dxcc' in r:
                dxcc = str(r.replace("dxcc:", ""))
                log = log[log["dxcc"] == dxcc]
                cumulated_info.append(r)
            if 'cq' in r:
                zonecq = int(r.replace("cq:", ""))
                log = log[log["zonecq"] == zonecq]
                cumulated_info.append(r)
            if 'points' in r:
                points = int(r.replace("points:", ""))
                log = log[log["points"] == points]
                cumulated_info.append(r)
            if 'maxRate_1min' in r:
                log = log[log["maxRate_1min"] == 1]
                cumulated_info.append(r)
            if 'maxRate_5min' in r:
                log = log[log["maxRate_5min"] == 1]
                cumulated_info.append(r)
            if 'maxRate_10min' in r:
                log = log[log["maxRate_10min"] == 1]
                cumulated_info.append(r)
            if 'maxRate_30min' in r:
                log = log[log["maxRate_30min"] == 1]
                cumulated_info.append(r)
            if 'maxRate_60min' in r:
                log = log[log["maxRate_60min"] == 1]
                cumulated_info.append(r)
            if 'maxRate_120min' in r:
                log = log[log["maxRate_120min"] == 1]
                cumulated_info.append(r)
        cumulated_info = ','.join(cumulated_info)

    cumulated_unique_band = []
    if request.GET.get('unique_band'):
        rule = str(request.GET['unique_band']).split(",")
        for r in rule:
            if 'call' in r:
                log = log.groupby(["call", "band"], sort=False, as_index=False).first()
                cumulated_unique_band.append(r)
            if 'freq' in r:
                log = log.groupby(["frequency", "band"], sort=False, as_index=False).first()
                cumulated_unique_band.append(r)
            if 'date' in r:
                log = log.groupby(["date", "band"], sort=False, as_index=False).first()
                cumulated_unique_band.append(r)
            if 'time' in r:
                log = log.groupby(["time", "band"], sort=False, as_index=False).first()
                cumulated_unique_band.append(r)
            if 'cont' in r:
                log = log.groupby(["continent", "band"], sort=False, as_index=False).first()
                cumulated_unique_band.append(r)
            if 'dxcc' in r:
                log = log.groupby(["dxcc", "band"], sort=False, as_index=False).first()
                cumulated_unique_band.append(r)
            if 'cq' in r:
                log = log.groupby(["zonecq", "band"], sort=False, as_index=False).first()
                cumulated_unique_band.append(r)
        cumulated_unique_band = ','.join(cumulated_unique_band)

    cumulated_unique = []
    if request.GET.get('unique'):
        rule = str(request.GET['unique']).split(",")
        for r in rule:
            if "band" in r:
                log = log.groupby(["band"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
            if 'call' in r:
                log = log.groupby(["call"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
            if 'freq' in r:
                log = log.groupby(["frequency"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
            if 'date' in r:
                log = log.groupby(["date"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
            if 'time' in r:
                log = log.groupby(["time"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
            if 'cont' in r:
                log = log.groupby(["continent"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
            if 'dxcc' in r:
                log = log.groupby(["dxcc"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
            if 'cq' in r:
                log = log.groupby(["zonecq"], sort=False, as_index=False).first()
                cumulated_unique.append(r)
        cumulated_unique = ','.join(cumulated_unique)

    filtered_length = len(log)

    page = 1
    if request.GET.get('filter'):
        rule = str(request.GET['filter']).split(",")
        for r in rule:
            if "page" in r:
                page = int(r.replace("page:", ""))
    log = log[(page-1)*qsos_page:page*qsos_page]

    num_pages = []
    for i in range(1, int(round(filtered_length/float(qsos_page), 0) + 1)):
        num_pages.append(i)

    log_info = []
    for index, row in log.iterrows():
        log_info.append([
            row["counter"],
            row["band"],
            row["frequency"],
            row["date"],
            row["time"],
            row["call"],
            row["continent"],
            row["dxcc"],
            row["zonecq"],
            row["points"],
            ])

    return render(request, 'analysis_log.html', {"log_info": log_info, 'cumulated_info': cumulated_info,
                                                 'cumulated_unique': cumulated_unique,
                                                 'cumulated_unique_band': cumulated_unique_band, 'page': page,
                                                 'num_pages': num_pages, 'total_pages': len(num_pages), 'nbar': 'log',
                                                 'latbar':'log'
                                                 }
                  )


# ________________________________________________________________________________________________________
def contest_rates(request):
    # --- Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # --- Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)
    rates = contest.max_rates

    rates_info = []
    rates_info.append(["1",   rates["1min"][0],   rates["1min"][0]/1.,     rates["1min"][0]*60./1.,     str(rates["1min"][1][0]),  str(rates["1min"][1][1])])
    rates_info.append(["5",   rates["5min"][0],   rates["5min"][0]/5.,     rates["5min"][0]*60./5.,     str(rates["5min"][1][0]),  str(rates["5min"][1][1])])
    rates_info.append(["10",  rates["10min"][0],  rates["10min"][0]/10.,   rates["10min"][0]*60./10.,   str(rates["10min"][1][0]),  str(rates["10min"][1][1])])
    rates_info.append(["30",  rates["30min"][0],  rates["30min"][0]/30.,   rates["30min"][0]*60./30.,   str(rates["30min"][1][0]),  str(rates["30min"][1][1])])
    rates_info.append(["60",  rates["60min"][0],  rates["60min"][0]/60.,   rates["60min"][0]*60./60.,   str(rates["60min"][1][0]),  str(rates["60min"][1][1])])
    rates_info.append(["120", rates["120min"][0], rates["120min"][0]/120., rates["120min"][0]*60./120., str(rates["120min"][1][0]), str(rates["120min"][1][1])])

    return render(request, 'analysis_rates.html', {'rates_info': rates_info, 'nbar': 'rates'})


#________________________________________________________________________________________________________
def contest_rates_per_minute(request):
    # Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)

    list_rates = contest.ratesPerMinute

    range_mins = []
    for i in range(60):
        range_mins.append(str(i).zfill(2))

    days = list(contest.log.groupby("date").groups.keys())
    days.sort()

    range_hours = []
    for i in range(24):
        range_hours.append(str(i).zfill(2))
    range_hours = range_hours*len(days)

    range_days = []
    for d in days:
        range_days += [d]*24

    # --- list_rates is a list made of 48 sub-lists. Each sub-list has 60 rates, for each minute in each hour of the
    # contest. Now we will convert each rate in a list of [min, rate]
    list_rates_min = []
    for h, lh in enumerate(list_rates):
        list_rates_min.append([])
        for m, lm in enumerate(lh):
            list_rates_min[h].append([str(m).zfill(2), lm])

    return render(request, 'analysis_rate_per_min.html', {'list_rates': zip(range_days, range_hours, list_rates_min),
                                                          'range_mins': range_mins, 'nbar': 'rates'
                                                          }
                  )


# ________________________________________________________________________________________________________
def contest_dxcc_frequency(request):
    # --- Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # --- Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)

    qsos_page = 10

    log = contest.log
    cumulated_info = []
    if request.GET.get('filter'):
        rule = str(request.GET['filter']).split(",")
        for r in rule:
            if "band" in r:
                band = int(r.replace("band:", ""))
                log = log[log["band"]==band]
                cumulated_info.append(r)
            if 'date' in r:
                date = str(r.replace("date:", ""))
                log = log[log["date"]==date]
                cumulated_info.append(r)
            if 'time' in r:
                time = str(r.replace("time:", ""))
                log = log[log["time"]==time]
                cumulated_info.append(r)
            if 'dxcc' in r:
                dxcc = str(r.replace("dxcc:", ""))
                log = log[log["dxcc"]==dxcc]
                cumulated_info.append(r)
        cumulated_info = ','.join(cumulated_info)

    page = 1
    if request.GET.get('filter'):
        rule = str(request.GET['filter']).split(",")
        for r in rule:
            if "page" in r:
                page = int(r.replace("page:", ""))

    grouped_counts = log.groupby("dxcc")["dxcc"].count()
    counts = grouped_counts.tolist()
    names = grouped_counts.index.tolist()

    num_pages = []
    filtered_length = len(grouped_counts)
    for i in range(1, int(round(filtered_length/float(qsos_page), 0) + 1)):
        num_pages.append(i)

    list_dxcc = []
    for n, c in zip(names, counts):
        list_dxcc.append([n, c])

    from operator import itemgetter
    list_dxcc = sorted(list_dxcc, key=itemgetter(1))
    list_dxcc = list(reversed(list_dxcc))

    list_dxcc = list_dxcc[(page-1)*qsos_page:page*qsos_page]

    return render(request, 'analysis_dxccfreq.html', {'list_dxcc': list_dxcc, 'page':page, 'num_pages':num_pages,
                                                      'total_pages': len(num_pages), 'nbar': 'log'
                                                      }
                  )


#________________________________________________________________________________________________________
def contest_plots(request):
    # Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)

    # Get keys from link
    plot_key = "dummie"
    if request.GET.get('chart'):
        plot_key = str(request.GET.get('chart'))

    options = ""
    if request.GET.get('options'):
        options = str(request.GET.get('options'))
    else:
        if request.GET.get('band'):
            options += "band%s,"%str(request.GET.get('band'))
        if request.GET.get('continent'):
            options += "continent%s,"%str(request.GET.get('continent'))
        if request.GET.get('station_type'):
            options += "%s,"%str(request.GET.get('station_type'))
        if request.GET.get('avg'):
            options += "avg%s,"%str(request.GET.get('avg'))
        if request.GET.get('fromto'):
            fromto = str(request.GET.get('fromto'))
            options += "from%s,to%s,"%(fromto[0:4], fromto[4:8])
        options = options[:-1]

    # Generate code to inject to html

    plot_dict = plot_dictionary
    plot_snippet = ""
    for plot in plot_dict.names():
        if plot == plot_key:
            plot_snippet = plot_dict.plots()[plot_key].do_plot(contest=contest, doSave=True, options=options)

    # Mark active block in html
    nbar=""
    if plot_key=='plot_qsos_vs_time__band':
        nbar="rates"
    if plot_key=='plot_qsos_vs_time__continent':
        nbar="rates"
    if plot_key=='plot_qsos_vs_time__stationtype':
        nbar="rates"
    if plot_key=='plot_fraction_stationtype':
        nbar="operation"
    if plot_key=='plot_ratio_qsos_min':
        nbar="rates"
    if plot_key=='plot_mults_vs_qsos':
        nbar="operation"
    if plot_key=='plot_time_vs_band_vs_continent':
        nbar="rates"
    if plot_key=='plot_freq_vs_date':
        nbar="operation"
    if plot_key=='plot_lenghtcallmorse':
        nbar="morse"
    if plot_key=='plot_heading':
        nbar="operation"
    if plot_key=='plot_db_vs_date':
        nbar="operation"
    if plot_key=='plot_cwspeed':
        nbar="morse"
    if plot_key == 'plot_cwsignal':
        nbar = "morse"

    #--- Lateral bar
    latbar = ""
    if "plot_qsos_vs_time__band" in plot_key:
        latbar = "qsos_vs_time__band"
    if "plot_ratio_qsos_min" in plot_key:
        latbar = "ratio_qsos_min"
    if "plot_heading" in plot_key:
        latbar = "heading"
    if "plot_db_vs_date" in plot_key:
        latbar = "db_vs_time"
    if plot_key=='plot_cwspeed':
        latbar="cwspeed"

    # Old options to retain
    old_options = ""
    for opt in options.split(","):
        if "plot_heading" in plot_key:
            if "from" in opt:
                old_options += opt+","
            if "to" in opt:
                old_options += opt+","
        if "plot_db_vs_date" in plot_key:
            if "continent" in opt:
                old_options += opt+","
            if "avg" in opt:
                old_options += opt+","

    return render(request, 'analysis_images.html', {"plot_snippet":plot_snippet, 'nbar':nbar, 'latbar':latbar, 'old_options':old_options})


#________________________________________________________________________________________________________
def maps(request):
    # Get info from form
    search_info = request.session['cleaned_data']
    if "new_callsign" in request.session.keys():
        request.session['cleaned_data']['callsign'] = request.session['new_callsign']

    # Retrieve contest object from pickle file
    contest = retrieve_contest_object(search_info=search_info, output_folder=output_folder)

    # Get keys from link
    options = ""
    options_str = ""
    if request.GET.get('options'):
        options = str(request.GET.get('options')).split(",")
    else:
        if request.GET.get('band'):
            options += "band%s,"%str(request.GET.get('band'))
        if request.GET.get('continent'):
            options += "continent%s,"%str(request.GET.get('continent'))
        if request.GET.get('fromto'):
            fromto = str(request.GET.get('fromto'))
            options += "from%s,to%s,"%(fromto[0:4], fromto[4:8])
        options = options[:-1].split(",")

    list_calls = None
    extra_conditions = (contest.log["band"]>0)
    for opt in options:
        if "band" in opt:
            options_str = opt+","
            band = int(opt.replace("band", ""))
            extra_conditions &= (contest.log["band"]==band)
        if "from" in opt:
            time_from = str(opt.replace("from", ""))
            extra_conditions &= (contest.log["time"]>=time_from)
        if "to" in opt:
            time_to   = str(opt.replace("to", ""))
            extra_conditions &= (contest.log["time"]<=time_to)
    list_calls = contest.log[extra_conditions][["call", "latitude", "longitude"]].dropna().values.tolist()

    list_calls.sort()
    list_calls_unique =  list(k for k,_ in itertools.groupby(list_calls))

    calls = list(k[0] for k in list_calls_unique)
    lat = list(k[1] for k in list_calls_unique)
    lon = list(k[2] for k in list_calls_unique)

    return render(request, 'analysis_maps.html', {'nbar':'maps', 'latbar':'maps', 'list_calls':zip(calls, lat, lon), 'mylat':contest.log["mylatitude"].iloc[0], 'mylon':contest.log["mylongitude"].iloc[0], 'old_options':options_str})

#________________________________________________________________________________________________________
def guestbook(request):
    from .forms import PostForm
    from django.utils import timezone
    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('contestAnalyzer:mainPage')
    else:
        form = PostForm()

    return render(request, 'guestbook.html', {'form':form})
