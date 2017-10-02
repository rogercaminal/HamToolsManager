import os
import ContestAnalyzerOnline.contestAnalyzer.toolBase
import pandas as pd
import numpy as np

class tool_band(ContestAnalyzerOnline.contestAnalyzer.toolBase.toolBase):
    def applyToAll(self, contest):
        contest.log["band"] = np.where((contest.log["frequency"]>=1800 ) & (contest.log["frequency"]<1900 ), 160,
                              np.where((contest.log["frequency"]>=3500 ) & (contest.log["frequency"]<3900 ), 80,
                              np.where((contest.log["frequency"]>=7000 ) & (contest.log["frequency"]<7500 ), 40,
                              np.where((contest.log["frequency"]>=14000) & (contest.log["frequency"]<15000), 20,
                              np.where((contest.log["frequency"]>=21000) & (contest.log["frequency"]<22000), 15,
                              np.where((contest.log["frequency"]>=28000) & (contest.log["frequency"]<30000), 10, np.nan
              ))))))

        contest.log["band_int"] = np.where(contest.log["band"]==160, 6,
                               np.where(contest.log["band"]==80 , 5,
                               np.where(contest.log["band"]==40 , 4,
                               np.where(contest.log["band"]==20 , 3,
                               np.where(contest.log["band"]==15 , 2,
                               np.where(contest.log["band"]==10 , 1, np.nan
                      ))))))
