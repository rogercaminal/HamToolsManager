from ContestAnalyzerOnline.contestAnalyzer.tool_manager import ToolManager
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_counter import ToolCounter
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_datetime import ToolDatetime
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_maxrates import ToolMaxRates
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_hour import ToolHour
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_band import ToolBand
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_station_type import ToolStationType
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_getdxcc import ToolGetDXCC
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_contest_evolution import ToolContestEvolution
from ContestAnalyzerOnline.contestAnalyzer.tools.tool_lenghtcallmorse import ToolLenghtCallMorse

tool_dictionary = ToolManager()

tool_dictionary.add_tool("tool_counter", ToolCounter("tool_counter"))
tool_dictionary.add_tool("tool_datetime", ToolDatetime("tool_datetime"))
tool_dictionary.add_tool("tool_maxrates", ToolMaxRates("tool_maxrates"))
tool_dictionary.add_tool("tool_hour", ToolHour("tool_hour"))
tool_dictionary.add_tool("tool_band", ToolBand("tool_band"))
tool_dictionary.add_tool("tool_station_type", ToolStationType("tool_station_type"))
tool_dictionary.add_tool("tool_getdxcc", ToolGetDXCC("tool_getdxcc"))
tool_dictionary.add_tool("tool_contest_evolution", ToolContestEvolution("tool_contest_evolution"))
tool_dictionary.add_tool("tool_lenghtcallmorse", ToolLenghtCallMorse("tool_lenghtcallmorse"))