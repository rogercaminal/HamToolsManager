import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase

class plotManager(object):
    def __init__(self):
        self.m_names = []
        self.m_plots = {}

    def names(self):
        return self.m_names

    def plots(self):
        return self.m_plots

    def addPlot(self, name, plot):
        self.m_names.append(name)
        self.m_plots[name] = plot

    def reset(self):
        self.m_names.clear()
        self.m_plots.clear()
