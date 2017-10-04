import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_freq_vs_date(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        naxis = contest.log["stn"].max()

        fig, ax = plt.subplots(naxis+2, 1, sharex=True)
        fig.suptitle('Frequency vs time', fontsize=14, fontweight='bold')

        #--- Plot freq of QSO vs datetime
        ax[0].plot(contest.log["datetime"], contest.log["frequency"])
        ax[0].set_title("All stations")
        ax[0].set_ylabel("Frequency [MHz]")

        for i in range(0, naxis+1):
          ax[i+1].plot(contest.log[contest.log["stn"]==i]["datetime"], contest.log[contest.log["stn"]==i]["frequency"])
          ax[i+1].set_title("Station #%d"%i)
          ax[i+1].set_ylabel("Frequency [MHz]")

        ax[naxis+1].set_xlabel("date")

        print("The following plot shows the frequency evolution in the contest. The labeling from the different stations comes from the log.")
        
        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_freq_vs_time.png", bbox_inches='tight')
