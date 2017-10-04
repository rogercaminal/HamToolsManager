import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ContestAnalyzerOnline.contestAnalyzer.morseHelper

class plot_lenghtcallmorse(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave):
        fig, ax = plt.subplots(1, 1, sharex=True)
        fig.suptitle('Call length @ 35WPM', fontsize=12, fontweight='bold')

        #--- Plot QSOs per hour and station type
        qsos_running  = contest.log[(contest.log["station_type"]=="running") & (pd.isnull(contest.log["continent"])==False)]["hour"].count()
        qsos_inband   = contest.log[(contest.log["station_type"]=="inband")  & (pd.isnull(contest.log["continent"])==False)]["hour"].count()
        qsos_multi    = contest.log[(contest.log["station_type"]=="multi")   & (pd.isnull(contest.log["continent"])==False)]["hour"].count()

        ax.hist([contest.log["morse_length_seconds"]], bins=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0])
        ax.set_xlabel("Time [s]")

        mconvert = ContestAnalyzerOnline.contestAnalyzer.morseHelper.morse_converter(35)
        mconvert.setString("test %s %s" % (contest.callsign, contest.callsign))
        plt.axvline(mconvert.getTime(), color='r', linestyle='dashed', linewidth=2)
        ax.text(mconvert.getTime()+0.2, ax.get_ylim()[1]*0.75, 'TEST %s %s @ 30 WPM'%(contest.callsign, contest.callsign), fontsize=10, color="r")

        mconvert = ContestAnalyzerOnline.contestAnalyzer.morseHelper.morse_converter(40)
        mconvert.setString("test %s %s" % (contest.callsign, contest.callsign))
        plt.axvline(mconvert.getTime(), color='g', linestyle='dashed', linewidth=2)
        ax.text(mconvert.getTime()+0.2, ax.get_ylim()[1]*0.9, 'TEST %s %s @ 40 WPM'%(contest.callsign, contest.callsign), fontsize=10, color="g")

        print("Morse code call lengths from QSOs at a speed of 35 WPM. For reference, the length for \"TEST %s %s\" at 30 WPM and 40 WPM is shown. This can be useful to study the TX speed for inbands or 2BSIQ operations." % (contest.callsign, contest.callsign))
        
        if not doSave:
            plt.show()
        else:
            fig.savefig(contest.folderToSave+"plot_call_length_morse.png", bbox_inches='tight')
