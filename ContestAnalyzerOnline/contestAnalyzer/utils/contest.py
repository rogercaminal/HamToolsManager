#from urllib.request import urlopen

import logging

logging.basicConfig(format='%(levelname)s: %(asctime)s UTC  -  contest.py : %(message)s', level=logging.DEBUG)


def read_contest_general_info(contest, infile):
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


# ________________________________________________________________________________________________________

def retrieve_contest_object(search_info):
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
def print_contest_summary(contest):
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
