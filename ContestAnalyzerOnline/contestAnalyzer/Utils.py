import os
#from urllib.request import urlopen
from urllib2 import urlopen
import pandas as pd
import numpy as np

#--- Type of initial variables
dict_types = {}
dict_types["frequency"] = np.float64
dict_types["mode"]      = np.object
dict_types["date"]      = np.object
dict_types["time"]      = np.object
dict_types["mycall"]    = np.object
dict_types["urrst"]     = np.int64
dict_types["urnr"]      = np.int64
dict_types["call"]      = np.object
dict_types["myrst"]     = np.int64
dict_types["mynr"]      = np.int64
dict_types["ismult"]    = np.int64

#____________________________________________________________________________________________________________
def getLog(contestType, callsign, year, mode):
    isgood = False
    try:
        response = None
        if contestType=="cqww":
            print('Getting the log from http://www.cqww.com/publiclogs/%s%s/%s.log'%(year, mode, callsign.lower()))
            response = urlopen("http://www.cqww.com/publiclogs/%s%s/%s.log"%(year, mode, callsign.lower()))
        elif contestType=="cqwpx":
            print('Getting the log from http://www.cqwpx.com/publiclogs/%s%s/%s.log'%(year, mode, callsign.lower()))
            response = urlopen("http://www.cqwpx.com/publiclogs/%s%s/%s.log"%(year, mode, callsign.lower()))
        html = response.read()
        isgood = True
        return isgood, html
    except:
        return isgood, str("")


#____________________________________________________________________________________________________________
def getListOfLogs(contestType, year, mode):
    response = None
    if contestType=="cqww":
        response = urlopen("http://www.cqww.com/publiclogs/%s%s/"%(year, mode))
    elif contestType=="cqwpx":
        response = urlopen("http://www.cqwpx.com/publiclogs/%s%s/"%(year, mode, ))
    html = str(response.read())

    html = html[html.find("Number of logs found"):]
    calls = []
    for l in html.split("<"):
        if "a href=" in l:
            calls.append(l.split(">")[-1])
    del calls[calls.index("World Wide Radio Operators Foundation")]

    calls.sort()
    return calls


#____________________________________________________________________________________________________________
def getListOfYears(contestType):
    try:
        response = None
        if contestType=="cqww":
            response = urlopen("http://www.cqww.com/publiclogs/")
        elif contestType=="cqwpx":
            response = urlopen("http://www.cqwpx.com/publiclogs/")
        html = str(response.read())

        years = []
        for l in html.split("\n"):
            if "View CQ W" in l:
                year = l.split()[5]
                if year not in years:
                    years.append(year)

        years.sort()
        return years
    except:
        return ["2016"]


#________________________________________________________________________________________________________
def importLog(contest, contestType, year, mode, callsign, forceCSV=False):

    print "Importing contest object..."
    #--- Check if formatted pickle file exists and used unless otherwise specified
    if (not os.path.exists("%s.pickle" % contest.logName.replace(".log", ""))):

        print "Checking folders and creating them..."
        #--- Check if logfiles folder exists and create if not
        if (not os.path.exists("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/" % (contestType, year, mode, callsign))):
            os.makedirs("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/" % (contestType, year, mode, callsign))

        if (not os.path.exists("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/plots/" % (contestType, year, mode, callsign))):
            os.makedirs("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/plots/" % (contestType, year, mode, callsign))

        #--- Download log file from web
        isgood, downloadedlog = getLog(contestType, callsign, year, mode)
        if not isgood:
            return isgood, False

        infile = open(contest.logName, "wb")
        infile.write(downloadedlog)
        infile.close()

        print "Creating Pandas object..."
        #--- Create csv file header
        csvfile = open(contest.logName.replace(".log",".csv"), "w")
        csvfile.write("frequency,mode,date,time,mycall,urrst,urnr,call,myrst,mynr,stn\n")

        #--- Loop on lines info line by line to create data frame
        infile = open(contest.logName)
        lines = infile.readlines()
        for l in lines:
            line = l.split(":")[1].replace('\n', '')
            line = line[1:]
            if "QSO" in l:
                if len(line.split())==10:
                    line += ",0"
                line = ','.join(line.split())+"\n"
                csvfile.write(line)
        csvfile.close()
        infile.close()
        contest.log = pd.read_csv(contest.logName.replace(".log",".csv"), dtype=dict_types)
        os.remove(contest.logName.replace(".log",".csv"))

        #--- Read contest information for original log file
        infile = open(contest.logName)
        infile.seek(0)
        readContestGeneralInfo(contest, infile)
        infile.close()
        os.remove(contest.logName)

        return isgood, True

    return True, False


#________________________________________________________________________________________________________
def importReverseBeaconSpots(contest):
    print "Getting reverse beacon spots..."
    #--- Check if formatted pickle file exists and used unless otherwise specified
    if (not os.path.exists("%s.pickle" % contest.logName.replace(".log", ""))):

        from StringIO import StringIO
        import zipfile


        spots_list = []
        contest_dates = contest.log.groupby("date").groups.keys()
        contest_dates.sort()

        for d in contest_dates:
            date = d.replace("-","")
            try:
                myzipfile = zipfile.ZipFile(StringIO(urlopen("http://reversebeacon.net/raw_data/dl.php?f=%s"%date).read()))
            except:
                print "Problem getting reverse beacon spots"
                return False
            csvfile = [StringIO(myzipfile.read(name)) for name in myzipfile.namelist()]

            sp = pd.read_csv(csvfile[0], keep_default_na=False, dtype={"callsign":np.object, \
                    "de_pfx":np.object, \
                    "de_cont":np.object, \
                    "freq":np.object, \
                    "band":np.object, \
                    "dx":np.object, \
                    "dx_pfx":np.object, \
                    "dx_cont":np.object, \
                    "mode":np.object, \
                    #"db":np.int64, \
                    #"speed":np.int64, \
                    #"tx_mode":np.object\
                    })
            sp["date"]  = pd.to_datetime(sp["date"])
            sp["freq"]  = pd.to_numeric(sp["freq"])
            sp["speed"] = pd.to_numeric(sp["speed"])
            sp["db"]    = pd.to_numeric(sp["db"])

            sp["date_roundmin"] = sp["date"].dt.round("min")

            spots_list.append(sp[sp["dx"]==contest.callsign])
        contest.rbspots = pd.concat(spots_list)
        return True
    return True


#________________________________________________________________________________________________________
def readContestGeneralInfo(contest, infile):
    lines = infile.readlines()
    for l in lines:
        line = l.split(":")[1].replace('\n', '')
        line = line[1:]
        if "CALLSIGN" in l:
            contest.callsign = line
        if "CONTEST" in l:
            contest.contest = line
        if "CATEGORY-OPERATOR" in l:
            contest.cat_operator = line
        if "CATEGORY-ASSISTED" in l:
            contest.cat_assisted = line
        if "CATEGORY-BAND" in l:
            contest.cat_band = line
        if "CATEGORY-POWER" in l:
            contest.cat_power = line
        if "CATEGORY-MODE" in l:
            contest.cat_mode = line
        if "CATEGORY-TRANSMITTER" in l:
            contest.cat_transmitter = line
        if "NAME" in l:
            contest.name = line
        if "LOCATION" in l:
            contest.location = line
        if "OPERATORS" in l:
            contest.operators = line.split()
        if "CLUB" in l:
            contest.club = line
    infile.seek(0)
    contest.category = "%s %s %s %s %s %s" % (contest.cat_operator, contest.cat_transmitter, contest.cat_band, contest.cat_assisted, contest.cat_power, contest.cat_mode)


#________________________________________________________________________________________________________
def retrieveContestObject(search_info):
    contestType = search_info["name"]
    callsign    = search_info["callsign"]
    year        = search_info["year"]
    mode        = search_info["mode"]

    import pickle
    logname = "ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/log_%s_%s_%s_%s.log" % (contestType, year, mode, callsign, contestType, year, mode, callsign)

    contest = None
    with open("%s.pickle" % logname.replace(".log", ""), 'rb') as myinput:
        contest = pickle.load(myinput)
    return contest
    

#________________________________________________________________________________________________________
def printContestSummary(contest):
    print(contest)
    print()
    print('====================== S U M M A R Y =======================')
    print(str("BAND").ljust(15),
          str("QSOs").ljust(8),
          str("DXCC").ljust(8),
          str("Zn").ljust(8),
          str("Pts").ljust(8),
          str("Pts/QSO"))
    qsos_cumul = 0
    dxcc_cumul = 0
    zones_cumul = 0
    points_cumul = 0
    for band in [10, 15, 20, 40, 80, 160]:
        qsos   = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"]==band)]["call"].count()
        dxcc   = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"]==band)]["dxcc"].value_counts().count()
        zones  = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"]==band)]["mynr"].value_counts().count()
        points = contest.log[(contest.log["isdupe"]==False) & (contest.log["band"]==band)]["points"].sum()
        qsos_cumul   += qsos
        dxcc_cumul   += dxcc
        zones_cumul  += zones
        points_cumul += points
        print(str(band).ljust(15),
              str(qsos).ljust(8),
              str(dxcc).ljust(8),
              str(zones).ljust(8),
              str(points).ljust(8),
              str("%.2f" % (float(points)/qsos)).ljust(8))
    print('------------------------------------------------------------')
    print(str("TOTAL").ljust(15),
          str(qsos_cumul).ljust(8),
          str(dxcc_cumul).ljust(8),
          str(zones_cumul).ljust(8),
          str(points_cumul).ljust(8),
          str("%.2f" % (float(points)/qsos)).ljust(8),
          str("SCORE: %d" % ((zones_cumul+dxcc_cumul)*points_cumul)).ljust(8))
    print('\n')
