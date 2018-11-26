import pickle
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


def retrieve_contest_object(search_info):
    contestType = search_info["name"]
    callsign = search_info["callsign"]
    year = search_info["year"]
    mode = search_info["mode"]

    logname = "ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/log_%s_%s_%s_%s.log" % (contestType, year, mode, callsign, contestType, year, mode, callsign)

    contest = None
    with open("%s.pickle" % logname.replace(".log", ""), 'rb') as myinput:
        contest = pickle.load(myinput)
    return contest