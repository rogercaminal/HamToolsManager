import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_ratio_qsos_min(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        fig1, ax1 = plt.subplots(1, 1, sharex=True)
        fig2, ax2 = plt.subplots(1, 1, sharex=True)
        fig3, ax3 = plt.subplots(1, 1, sharex=True)
        fig1.suptitle('QSOs per min', fontsize=12, fontweight='bold')
        fig2.suptitle('QSOs per min', fontsize=12, fontweight='bold')
        fig3.suptitle('QSOs per min', fontsize=12, fontweight='bold')

        #--- Plot QSOs per hour and freq
        qsos_all_day1     = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0])]["datetime"].value_counts().fillna(0)
        qsos_all_day2     = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1])]["datetime"].value_counts().fillna(0)
        qsos_running_day1 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0]) & (contest.log["station_type"]=="running")]["datetime"].value_counts()
        qsos_running_day2 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1]) & (contest.log["station_type"]=="running")]["datetime"].value_counts()
        qsos_inband_day1  = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0]) & (contest.log["station_type"]=="inband")]["datetime"].value_counts()
        qsos_inband_day2  = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1]) & (contest.log["station_type"]=="inband")]["datetime"].value_counts()

        ax1.hist([qsos_all_day1, qsos_all_day2], range(1, 15), stacked=True, label=["Day 1", "Day 2"])
        ax1.set_title("All stations", fontsize=9)
        ax1.set_ylabel("# times")
        ax1.legend(prop={'size':10}, loc=1, ncol=3)

        ax2.hist([qsos_running_day1, qsos_running_day2], range(1, 15), stacked=True, label=["Day 1", "Day 2"])
        ax2.set_title("Running station(s)", fontsize=9)
        ax2.set_ylabel("# times")
        ax2.legend(prop={'size':10}, loc=1, ncol=3)

        ax3.hist([qsos_inband_day1, qsos_inband_day2], range(1, 15), stacked=True, label=["Day 1", "Day 2"])
        ax3.set_title("Inband station(s)", fontsize=9)
        ax3.set_ylabel("# times")
        ax3.set_xlabel("QSOs / min")
        ax3.legend(prop={'size':10}, loc=1, ncol=3)

        plt.setp(ax1, xticks=range(1,15))
        plt.setp(ax2, xticks=range(1,15))
        plt.setp(ax3, xticks=range(1,15))

        print("Number of QSOs per minute.")
        
        if not doSave:
            plt.show()
        else:
            fig1.savefig(contest.folderToSave+"plot_ratio_qsos_min.png", bbox_inches='tight')
            fig2.savefig(contest.folderToSave+"plot_ratio_qsos_min___running.png", bbox_inches='tight')
            fig3.savefig(contest.folderToSave+"plot_ratio_qsos_min___inband.png", bbox_inches='tight')

