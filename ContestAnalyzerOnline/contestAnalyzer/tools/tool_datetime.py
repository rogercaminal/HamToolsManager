from ContestAnalyzerOnline.contestAnalyzer.tools.tool_base import ToolBase
import pandas as pd

class ToolDatetime(ToolBase):
    def __init__(self, name):
        super(ToolDatetime, self).__init__(name)

    def apply_to_all(self, contest):
        contest.log["datetime"] = pd.Series(contest.log["date"] + " " + contest.log["time"], index=contest.log.index)
        contest.log["datetime"] = pd.to_datetime(contest.log["datetime"])
