import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_qsos_vs_time__band(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        fig, ax = plt.subplots(1, 1, sharex=True)
        fig.suptitle('QSOs per hour - band', fontsize=12, fontweight='bold')

        #--- Plot QSOs per hour and freq
        qsos10  = contest.log[(contest.log["band"]==10 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
        qsos15  = contest.log[(contest.log["band"]==15 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
        qsos20  = contest.log[(contest.log["band"]==20 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
        qsos40  = contest.log[(contest.log["band"]==40 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
        qsos80  = contest.log[(contest.log["band"]==80 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
        qsos160 = contest.log[(contest.log["band"]==160) & (pd.isnull(contest.log["continent"])==False)]["hour"]

        ax.hist([qsos10, qsos15, qsos20, qsos40, qsos80, qsos160], range(0, 48), stacked=True, label=["10m", "15m", "20m", "40m", "80m", "160m"])
        ax.set_xlim([0, 47])
        ax.set_ylabel("Hour")
        ax.legend(prop={'size':10}, loc=1, ncol=3)

        print("Number of QSOs per hour, separated by band.")
        
        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_qsos_vs_time__band.png", bbox_inches='tight')

