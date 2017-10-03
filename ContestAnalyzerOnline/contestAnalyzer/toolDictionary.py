import os
import ContestAnalyzerOnline.contestAnalyzer.toolManager
from ContestAnalyzerOnline.contestAnalyzer.toolLibrary import *

toolDictionary = ContestAnalyzerOnline.contestAnalyzer.toolManager.toolManager()

toolDictionary.addTool("tool_counter",           ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_counter.tool_counter("tool_counter"))
toolDictionary.addTool("tool_datetime",          ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_datetime.tool_datetime("tool_datetime"))
toolDictionary.addTool("tool_hour",              ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_hour.tool_hour("tool_hour"))
toolDictionary.addTool("tool_band",              ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_band.tool_band("tool_band"))
toolDictionary.addTool("tool_station_type",      ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_station_type.tool_station_type("tool_station_type"))
toolDictionary.addTool("tool_getdxcc",           ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_getdxcc.tool_getdxcc("tool_getdxcc"))
toolDictionary.addTool("tool_contest_evolution", ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_contest_evolution.tool_contest_evolution("tool_contest_evolution"))
toolDictionary.addTool("tool_lenghtcallmorse",   ContestAnalyzerOnline.contestAnalyzer.toolLibrary.tool_lenghtcallmorse.tool_lenghtcallmorse("tool_lenghtcallmorse"))
