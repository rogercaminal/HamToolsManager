import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_fraction_stationtype(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        fig, ax = plt.subplots(1, 1, sharex=True)
        fig.suptitle('QSO fraction - Station type', fontsize=12, fontweight='bold')

        #--- Plot QSOs per hour and station type
        qsos_running  = contest.log[(contest.log["station_type"]=="running") & (pd.isnull(contest.log["continent"])==False)]["hour"].count()
        qsos_inband   = contest.log[(contest.log["station_type"]=="inband")  & (pd.isnull(contest.log["continent"])==False)]["hour"].count()
        qsos_multi    = contest.log[(contest.log["station_type"]=="multi")   & (pd.isnull(contest.log["continent"])==False)]["hour"].count()

        ax.pie([qsos_running, qsos_inband, qsos_multi], labels=["Running", "Inband", "Multiplier"], autopct='%1.1f%%')
        ax.axis('equal')

        print("Fraction of QSOs for each station type.")
        
        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_fraction__stationtype.pdf", bbox_inches='tight')
