from ContestAnalyzerOnline.contestAnalyzer.tools.tool_base import ToolBase
import pandas as pd
import numpy as np

class ToolContestEvolution(ToolBase):

    def __init__(self, name):
        super(ToolContestEvolution, self).__init__(name)

    def apply_to_all(self, contest):
        
        #--- Count DXCC
        contest.log["cum_dxcc_band"]      = contest.log.groupby(["band", "dxcc"]).cumcount()+1
        contest.log["dxcc_band"]          = np.where(contest.log["cum_dxcc_band"]==1, 1, 0)
        contest.log["dxcc_band_evol_all"] = contest.log["dxcc_band"].cumsum()
        contest.log["dxcc_band_evol_10"]  = contest.log[contest.log["band"]==10]["dxcc_band"].cumsum()
        contest.log["dxcc_band_evol_15"]  = contest.log[contest.log["band"]==15]["dxcc_band"].cumsum()
        contest.log["dxcc_band_evol_20"]  = contest.log[contest.log["band"]==20]["dxcc_band"].cumsum()
        contest.log["dxcc_band_evol_40"]  = contest.log[contest.log["band"]==40]["dxcc_band"].cumsum()
        contest.log["dxcc_band_evol_80"]  = contest.log[contest.log["band"]==80]["dxcc_band"].cumsum()
        contest.log["dxcc_band_evol_160"] = contest.log[contest.log["band"]==160]["dxcc_band"].cumsum()
        
        #--- Count zones
        contest.log["cum_zonecq_band"]      = contest.log.groupby(["band", "mynr"]).cumcount()+1
        contest.log["zonecq_band"]          = np.where(contest.log["cum_zonecq_band"]==1, 1, 0)
        contest.log["zonecq_band_evol_all"] = contest.log["zonecq_band"].cumsum()
        contest.log["zonecq_band_evol_10"]  = contest.log[contest.log["band"]==10]["zonecq_band"].cumsum()
        contest.log["zonecq_band_evol_15"]  = contest.log[contest.log["band"]==15]["zonecq_band"].cumsum()
        contest.log["zonecq_band_evol_20"]  = contest.log[contest.log["band"]==20]["zonecq_band"].cumsum()
        contest.log["zonecq_band_evol_40"]  = contest.log[contest.log["band"]==40]["zonecq_band"].cumsum()
        contest.log["zonecq_band_evol_80"]  = contest.log[contest.log["band"]==80]["zonecq_band"].cumsum()
        contest.log["zonecq_band_evol_160"] = contest.log[contest.log["band"]==160]["zonecq_band"].cumsum()
        
        #--- Count multis (zones + dxcc)
        contest.log["mults_evol_all"] = contest.log["zonecq_band_evol_all"] + contest.log["dxcc_band_evol_all"]
        contest.log["mults_evol_10"]  = contest.log["zonecq_band_evol_10"]  + contest.log["dxcc_band_evol_10"]
        contest.log["mults_evol_15"]  = contest.log["zonecq_band_evol_15"]  + contest.log["dxcc_band_evol_15"]
        contest.log["mults_evol_20"]  = contest.log["zonecq_band_evol_20"]  + contest.log["dxcc_band_evol_20"]
        contest.log["mults_evol_40"]  = contest.log["zonecq_band_evol_40"]  + contest.log["dxcc_band_evol_40"]
        contest.log["mults_evol_80"]  = contest.log["zonecq_band_evol_80"]  + contest.log["dxcc_band_evol_80"]
        contest.log["mults_evol_160"] = contest.log["zonecq_band_evol_160"] + contest.log["dxcc_band_evol_160"]
        
        #--- Count dupes
        contest.log["call_counter_band"] = contest.log.groupby(["band", "call"]).cumcount()+1
        contest.log["isdupe"] = np.where(contest.log["call_counter_band"]>1, 1, 0)
        
        #--- Count QSOs 
        contest.log["qsos_counter_band"] = contest.log[contest.log["isdupe"]==0].groupby(["band", "call"]).cumcount()+1
        contest.log["qsos_evol_all"] = contest.log["qsos_counter_band"].cumsum()
        contest.log["qsos_evol_10"]  = contest.log[contest.log["band"]==10]["qsos_counter_band"].cumsum()
        contest.log["qsos_evol_15"]  = contest.log[contest.log["band"]==15]["qsos_counter_band"].cumsum()
        contest.log["qsos_evol_20"]  = contest.log[contest.log["band"]==20]["qsos_counter_band"].cumsum()
        contest.log["qsos_evol_40"]  = contest.log[contest.log["band"]==40]["qsos_counter_band"].cumsum()
        contest.log["qsos_evol_80"]  = contest.log[contest.log["band"]==80]["qsos_counter_band"].cumsum()
        contest.log["qsos_evol_160"] = contest.log[contest.log["band"]==160]["qsos_counter_band"].cumsum()
        
#        #--- Count points
        contest.log["points"] = np.where((contest.log["continent"]==contest.log["mycontinent"]) & (contest.log["isdupe"]==0) & (pd.isnull(contest.log["continent"])==False), 1, \
                                np.where((contest.log["continent"]!=contest.log["mycontinent"]) & (contest.log["isdupe"]==0) & (pd.isnull(contest.log["continent"])==False), 3, 0))
