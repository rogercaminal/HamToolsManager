import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_qsos_vs_time__stationtype(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        fig, ax = plt.subplots(1, 1, sharex=True)
        fig.suptitle('QSOs per hour - Station type', fontsize=12, fontweight='bold')

        #--- Plot QSOs per hour and station type
        qsos_running  = contest.log[(contest.log["station_type"]=="running") & (pd.isnull(contest.log["continent"])==False)]["hour"]
        qsos_inband   = contest.log[(contest.log["station_type"]=="inband")  & (pd.isnull(contest.log["continent"])==False)]["hour"]
        qsos_multi    = contest.log[(contest.log["station_type"]=="multi")   & (pd.isnull(contest.log["continent"])==False)]["hour"]

        ax.hist([qsos_running, qsos_inband, qsos_multi], range(0, 48), stacked=True, label=["Running", "Inband", "Multiplier"])
        ax.set_xlim([0, 47])
        ax.set_ylabel("Hour")
        ax.legend(prop={'size':10}, loc=1, ncol=3)

        print("Number of QSOs per hour, separated by station type.")
        
        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_qsos_vs_time__stationtype.pdf", bbox_inches='tight')
