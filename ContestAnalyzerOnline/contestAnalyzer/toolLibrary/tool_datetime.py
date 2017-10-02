import os
import ContestAnalyzerOnline.contestAnalyzer.toolBase
import pandas as pd
import numpy as np

class tool_datetime(ContestAnalyzerOnline.contestAnalyzer.toolBase.toolBase):
    def applyToAll(self, contest):
        contest.log["datetime"] = pd.Series(contest.log["date"] + " " + contest.log["time"], index=contest.log.index)
        contest.log["datetime"] = pd.to_datetime(contest.log["datetime"])
