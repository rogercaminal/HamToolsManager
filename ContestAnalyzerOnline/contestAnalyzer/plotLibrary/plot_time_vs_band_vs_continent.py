import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_time_vs_band_vs_continent(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):        
        fig, ax = plt.subplots(3, 2, sharex=True, sharey=True)
        fig.suptitle('Time vs band vs continent', fontsize=14, fontweight='bold')

        continents = ["continentEU", "continentNA", "continentSA", "continentAF", "continentOC", "continentAS"]
        for j in range(2):
            for i in range(3):
                ax[i, j].hist2d(contest.log[contest.log["continent"]==continents[i+3*j]]["hour"].values, contest.log[contest.log["continent"]==continents[i+3*j]]["band_int"].values, bins=[range(0,48), range(1,8)])
                ax[i, j].set_title(continents[i+3*j].replace("continent", ""))
                ax[i, j].set_yticklabels(["10 m", "15 m", "20 m", "40 m", "80 m", "160 m"])
                ax[i, j].set_ylim([1,7])
                if j%2==0:
                    ax[i, j].set_ylabel("band")
            ax[i, j].set_xlabel("hour")

        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_time_vs_band_vs_continent.png", bbox_inches='tight')
