import os
import ContestAnalyzerOnline.contestAnalyzer.toolBase
import pandas as pd
import numpy as np

class tool_hour(ContestAnalyzerOnline.contestAnalyzer.toolBase.toolBase):
    def applyToAll(self, contest):
        contest.log["hour"] = contest.log["datetime"].dt.hour + 24*(contest.log["datetime"].dt.day - contest.log["datetime"].dt.day[0])
