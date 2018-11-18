from ContestAnalyzerOnline.contestAnalyzer.tools.tool_base import ToolBase

class ToolCounter(ToolBase):

    def __init__(self, name):
        super(ToolCounter, self).__init__(name)

    def apply_to_all(self, contest):
        contest.log["counter"] = range(1, len(contest.log)+1)
