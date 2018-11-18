import logging
import os
#from urllib.request import urlopen
from urllib2 import urlopen
import pandas as pd
import numpy as np

from ContestAnalyzerOnline.contestAnalyzer.utils.contest import read_contest_general_info


def get_log(contestType, callsign, year, mode):
    isgood = False
    try:
        response = None
        if contestType=="cqww":
            logging.info('Getting the log from http://www.cqww.com/publiclogs/%s%s/%s.log'%(year, mode, callsign.lower()))
            response = urlopen("http://www.cqww.com/publiclogs/%s%s/%s.log"%(year, mode, callsign.lower()))
        elif contestType=="cqwpx":
            logging.info('Getting the log from http://www.cqwpx.com/publiclogs/%s%s/%s.log'%(year, mode, callsign.lower()))
            response = urlopen("http://www.cqwpx.com/publiclogs/%s%s/%s.log"%(year, mode, callsign.lower()))
        html = response.read()
        isgood = True
        return isgood, html
    except:
        return isgood, str("")


def get_list_of_logs(contestType, year, mode):
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


def get_list_of_years(contestType):
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


def import_log(contest, contestType, year, mode, callsign, forceCSV=False):

    # --- Type of initial variables
    dict_types = {}
    dict_types["frequency"] = np.float64
    dict_types["mode"] = np.object
    dict_types["date"] = np.object
    dict_types["time"] = np.object
    dict_types["mycall"] = np.object
    dict_types["urrst"] = np.int64
    dict_types["urnr"] = np.int64
    dict_types["call"] = np.object
    dict_types["myrst"] = np.int64
    dict_types["mynr"] = np.int64
    dict_types["ismult"] = np.int64

    logging.info("Importing contest object")
    #--- Check if formatted pickle file exists and used unless otherwise specified
    if (not os.path.exists("%s.pickle" % contest.log_name.replace(".log", ""))):

        logging.info("Checking folders and creating them")
        #--- Check if logfiles folder exists and create if not
        if (not os.path.exists("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/" % (contestType, year, mode, callsign))):
            os.makedirs("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/" % (contestType, year, mode, callsign))

        if (not os.path.exists("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/plots/" % (contestType, year, mode, callsign))):
            os.makedirs("ContestAnalyzerOnline/contestAnalyzer/data/%s_%s_%s_%s/plots/" % (contestType, year, mode, callsign))

        #--- Download log file from web
        isgood, downloadedlog = get_log(contestType, callsign, year, mode)
        if not isgood:
            return isgood, False

        infile = open(contest.log_name, "wb")
        infile.write(downloadedlog)
        infile.close()

        logging.info("Creating Pandas object")
        #--- Create csv file header
        csvfile = open(contest.log_name.replace(".log",".csv"), "w")
        csvfile.write("frequency,mode,date,time,mycall,urrst,urnr,call,myrst,mynr,stn\n")

        #--- Loop on lines info line by line to create data frame
        infile = open(contest.log_name)
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
        contest.log = pd.read_csv(contest.log_name.replace(".log",".csv"), dtype=dict_types)
        os.remove(contest.log_name.replace(".log",".csv"))

        #--- Read contest information for original log file
        infile = open(contest.log_name)
        infile.seek(0)
        read_contest_general_info(contest, infile)
        infile.close()
        os.remove(contest.log_name)

        return isgood, True

    return True, False