import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_ratio_qsos_min(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        fig, ax = plt.subplots(3, 1, sharex=True)
        fig.suptitle('QSOs per min', fontsize=12, fontweight='bold')

        #--- Plot QSOs per hour and freq
        qsos_all_day1     = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0])]["datetime"].value_counts().fillna(0)
        qsos_all_day2     = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1])]["datetime"].value_counts().fillna(0)
        qsos_running_day1 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0]) & (contest.log["station_type"]=="running")]["datetime"].value_counts()
        qsos_running_day2 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1]) & (contest.log["station_type"]=="running")]["datetime"].value_counts()
        qsos_inband_day1  = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0]) & (contest.log["station_type"]=="inband")]["datetime"].value_counts()
        qsos_inband_day2  = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1]) & (contest.log["station_type"]=="inband")]["datetime"].value_counts()

        ax[0].hist([qsos_all_day1, qsos_all_day2], range(1, 15), stacked=True, label=["Day 1", "Day 2"])
        ax[0].set_title("All stations", fontsize=9)
        ax[0].set_ylabel("# times")
        ax[0].legend(prop={'size':10}, loc=1, ncol=3)

        ax[1].hist([qsos_running_day1, qsos_running_day2], range(1, 15), stacked=True, label=["Day 1", "Day 2"])
        ax[1].set_title("Running station(s)", fontsize=9)
        ax[1].set_ylabel("# times")
        ax[1].legend(prop={'size':10}, loc=1, ncol=3)

        ax[2].hist([qsos_inband_day1, qsos_inband_day2], range(1, 15), stacked=True, label=["Day 1", "Day 2"])
        ax[2].set_title("Inband station(s)", fontsize=9)
        ax[2].set_ylabel("# times")
        ax[2].set_xlabel("QSOs / min")
        ax[2].legend(prop={'size':10}, loc=1, ncol=3)

        plt.setp(ax, xticks=range(1,15))

        print("Number of QSOs per minute.")
        
        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_qsos_vs_time__band.png", bbox_inches='tight')

