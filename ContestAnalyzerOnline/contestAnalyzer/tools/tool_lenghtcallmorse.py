from ContestAnalyzerOnline.contestAnalyzer.tools.tool_base import ToolBase
from ContestAnalyzerOnline.contestAnalyzer.utils.morse import MorseConverter

class ToolLenghtCallMorse(ToolBase):

    def __init__(self, name):
        super(ToolLenghtCallMorse, self).__init__(name)

    def apply_to_row(self, row):
        mconvert = MorseConverter(30)
        mconvert.setString(row["call"])
        time = mconvert.getTime()
        row["morse_length_seconds"] = time
        return row
