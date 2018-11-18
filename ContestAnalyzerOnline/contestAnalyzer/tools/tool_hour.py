from ContestAnalyzerOnline.contestAnalyzer.tools.tool_base import ToolBase

class ToolHour(ToolBase):

    def __init__(self, name):
        super(ToolHour, self).__init__(name)

    def apply_to_all(self, contest):
        contest.log["hour"] = contest.log["datetime"].dt.hour + 24*(contest.log["datetime"].dt.day - contest.log["datetime"].dt.day[0])
