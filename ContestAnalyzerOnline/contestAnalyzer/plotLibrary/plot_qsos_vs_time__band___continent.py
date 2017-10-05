import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class plot_qsos_vs_time__band___continent(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
#    def doPlot(self, contest, doSave):
#
#        #--- Get list of different DXCCs
#        countries = contest.log.groupby("dxcc").groups.keys()
#        countries.sort()
#
#        #--- Start plotting
#        print("DXCC for each hour, separated per band")
#        for i, dxcc in enumerate(countries):
#
#            fig, ax = plt.subplots(1, 1)
#            fig.suptitle('DXCC per hour - band', fontsize=12, fontweight='bold')
#
#            #--- Plot QSOs per hour and freq
#            qsos10  = contest.log[(contest.log["band"]==10 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["dxcc"]==dxcc)]["hour"]
#            qsos15  = contest.log[(contest.log["band"]==15 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["dxcc"]==dxcc)]["hour"]
#            qsos20  = contest.log[(contest.log["band"]==20 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["dxcc"]==dxcc)]["hour"]
#            qsos40  = contest.log[(contest.log["band"]==40 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["dxcc"]==dxcc)]["hour"]
#            qsos80  = contest.log[(contest.log["band"]==80 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["dxcc"]==dxcc)]["hour"]
#            qsos160 = contest.log[(contest.log["band"]==160) & (pd.isnull(contest.log["continent"])==False) & (contest.log["dxcc"]==dxcc)]["hour"]
#
#            try:
#                ax.hist([qsos10, qsos15, qsos20, qsos40, qsos80, qsos160], range(0, 48), stacked=True, label=["10m", "15m", "20m", "40m", "80m", "160m"])
#            except:
#                print "===> Cannot plot %d - %s - %d - %d - %d - %d - %d - %d" % (i, dxcc, len(qsos10), len(qsos15), len(qsos20), len(qsos40), len(qsos80), len(qsos160))
#            ax.set_xlabel("# QSOs")
#            ax.set_xlim([0, 47])
#            ax.set_ylabel("Hour")
#            ax.set_title(dxcc)
#            ax.legend(prop={'size':10}, loc=1, ncol=4)
#
#            if not doSave:
#                plt.show()
#            else:
#                fig.savefig(contest.folderToSave+"plot_dxcc_vs_time___band___%s.png"%dxcc.replace(" ", ""), bbox_inches='tight')
#            del fig, ax

    def doPlot(self, contest, doSave):

        #--- Get list of different DXCCs
        continents = contest.log.groupby("continent").groups.keys()
        continents.sort()

        #--- Start plotting
        print("Number of QSOs per hour and band, separated by continent")
        for i, continent in enumerate(continents):

            fig, ax = plt.subplots(1, 1)
            fig.suptitle('DXCC per hour - band', fontsize=12, fontweight='bold')

            #--- Plot QSOs per hour and freq
            qsos10  = contest.log[(contest.log["band"]==10 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos15  = contest.log[(contest.log["band"]==15 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos20  = contest.log[(contest.log["band"]==20 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos40  = contest.log[(contest.log["band"]==40 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos80  = contest.log[(contest.log["band"]==80 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos160 = contest.log[(contest.log["band"]==160) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]

            try:
                ax.hist([qsos10, qsos15, qsos20, qsos40, qsos80, qsos160], range(0, 48), stacked=True, label=["10m", "15m", "20m", "40m", "80m", "160m"])
            except:
                print "===> Cannot plot %d - %s - %d - %d - %d - %d - %d - %d" % (i, continent, len(qsos10), len(qsos15), len(qsos20), len(qsos40), len(qsos80), len(qsos160))
            ax.set_xlabel("# QSOs")
            ax.set_xlim([0, 47])
            ax.set_ylabel("Hour")
            ax.set_title(continent.replace("continent", ""))
            ax.legend(prop={'size':10}, loc=1, ncol=3)

            if not doSave:
                plt.show()
            else:
                fig.savefig(contest.folderToSave+"plot_qsos_vs_time__band___%s.png"%continent.replace(" ", ""), bbox_inches='tight')
            del fig, ax

