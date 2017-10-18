import os
import ContestAnalyzerOnline.contestAnalyzer.plotManager
from ContestAnalyzerOnline.contestAnalyzer.plotLibrary import *

plotDictionary = ContestAnalyzerOnline.contestAnalyzer.plotManager.plotManager()

plotDictionary.addPlot("plot_qsos_vs_time__band",        ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_qsos_vs_time__band.plot_qsos_vs_time__band("plot_qsos_vs_time__band"))
plotDictionary.addPlot("plot_qsos_vs_time__continent",   ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_qsos_vs_time__continent.plot_qsos_vs_time__continent("plot_qsos_vs_time__continent"))
plotDictionary.addPlot("plot_qsos_vs_time__stationtype", ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_qsos_vs_time__stationtype.plot_qsos_vs_time__stationtype("plot_qsos_vs_time__stationtype"))
plotDictionary.addPlot("plot_fraction_stationtype",      ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_fraction_stationtype.plot_fraction_stationtype("plot_fraction_stationtype"))
plotDictionary.addPlot("plot_ratio_qsos_min",            ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_ratio_qsos_min.plot_ratio_qsos_min("plot_ratio_qsos_min"))
plotDictionary.addPlot("plot_mults_vs_qsos",             ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_mults_vs_qsos.plot_mults_vs_qsos("plot_mults_vs_qsos"))
plotDictionary.addPlot("plot_time_vs_band_vs_continent", ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_time_vs_band_vs_continent.plot_time_vs_band_vs_continent("plot_time_vs_band_vs_continent"))
plotDictionary.addPlot("plot_freq_vs_date",              ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_freq_vs_date.plot_freq_vs_date("plot_freq_vs_date"))
plotDictionary.addPlot("plot_lenghtcallmorse",           ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_lenghtcallmorse.plot_lenghtcallmorse("plot_lenghtcallmorse"))
plotDictionary.addPlot("plot_heading",                   ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_heading.plot_heading("plot_heading"))
plotDictionary.addPlot("plot_db_vs_date",                ContestAnalyzerOnline.contestAnalyzer.plotLibrary.plot_db_vs_date.plot_db_vs_date("plot_db_vs_date"))
