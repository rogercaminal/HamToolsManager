import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_mults_vs_qsos(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):

        fig, ax = plt.subplots(1, 1, sharex=True)
        fig.suptitle('Mults vs QSOs', fontsize=14, fontweight='bold')

        #--- Plots
        ax.plot(contest.log["qsos_evol_all"], contest.log["mults_evol_all"], label="%s (current)"%(contest.callsign))
        ax.set_xlabel("QSOs")
        ax.set_ylabel("Multipliers")

        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_mults_vs_qsos.png", bbox_inches='tight')
