import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_qsos_vs_time__continent(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        fig, ax = plt.subplots(1, 1, sharex=True)
        fig.suptitle('QSOs per hour - continent', fontsize=12, fontweight='bold')

        #--- Plot QSOs per hour and freq
        qsosEU  = contest.log[contest.log["continent"]=="continentEU"]["hour"]
        qsosNA  = contest.log[contest.log["continent"]=="continentNA"]["hour"]
        qsosSA  = contest.log[contest.log["continent"]=="continentSA"]["hour"]
        qsosAF  = contest.log[contest.log["continent"]=="continentAF"]["hour"]
        qsosOC  = contest.log[contest.log["continent"]=="continentOC"]["hour"]
        qsosAN  = contest.log[contest.log["continent"]=="continentAN"]["hour"]
        qsosAS  = contest.log[contest.log["continent"]=="continentAS"]["hour"]

        ax.hist([qsosAF, qsosAN, qsosAS, qsosEU, qsosNA, qsosOC, qsosSA], range(0, 48), stacked=True, label=["AF", "AN", "AS", "EU", "NA", "OC", "SA"])
        ax.set_xlabel("# QSOs")
        ax.set_xlim([0, 47])
        ax.set_ylabel("Hour")
        ax.legend(prop={'size':10}, loc=1, ncol=4)

        print("Number of QSOs per hour, separated by continent.")
        
        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_qsos_vs_time__continent.png", bbox_inches='tight')

