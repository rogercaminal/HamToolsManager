import os
import ContestAnalyzerOnline.contestAnalyzer.toolBase
import pandas as pd
import numpy as np
from datetime import timedelta, date

class tool_maxrates(ContestAnalyzerOnline.contestAnalyzer.toolBase.toolBase):
    def applyToAll(self, contest):

        #--- Define function to compute time ranges
        def daterange(time_start, time_end):
            r = []
            for d in range(2):
                for n in range(0, int((time_end - time_start).seconds), 60):
                    r.append(time_start + timedelta(days=d, seconds=n))
            return r

        #--- Get initial and final times
        time_start = contest.log["datetime"].iloc[0]
        time_end = contest.log["datetime"].iloc[-1]
        date_range = daterange(time_start, time_end)

        #--- Steps to compute
        steps = [1, 5, 10, 30, 60, 120]

        #--- Get max rates
        for mins in steps:
            max_qsos = 0
            max_date = []
            for d in range(0, len(date_range)-mins):
                qsos = contest.log[(contest.log["datetime"]>=date_range[d]) & (contest.log["datetime"]<date_range[d+mins])]["call"].count()
                if qsos>max_qsos:
                    max_qsos = qsos
                    max_date = [date_range[d], date_range[d+mins]]
            contest.maxRates["%dmin"%mins] = [max_qsos, max_date]

        #--- Mark selected QSOs in log
        for mins in steps:
            contest.log["maxRate_%dmin"%mins] = np.where(
                    ((contest.log["datetime"]>=contest.maxRates["%dmin"%mins][1][0]) & (contest.log["datetime"]<contest.maxRates["%dmin"%mins][1][1])),
                    1,
                    0)

        #--- Store list of rates per minute of contest
        listDates = list(contest.log.groupby("date").groups.keys())
        listDates.sort()

        listRates = []
        for i, date in enumerate(listDates):
            for h in range(24):
                listRates.append([])
                for m in range(60):
                    time = "%s%s"%(str(h).zfill(2), str(m).zfill(2))
                    counts = contest.log[(contest.log["date"]==date) & (contest.log["time"]==time)]["call"].count()
                    listRates[h+i*24].append(counts)
        contest.ratesPerMinute = listRates
