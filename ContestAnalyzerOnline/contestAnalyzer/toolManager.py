import os
import ContestAnalyzerOnline.contestAnalyzer.toolBase

class toolManager(object):
    def __init__(self):
        self.m_names = []
        self.m_tools = {}

    def names(self):
        return self.m_names

    def tools(self):
        return self.m_tools

    def addTool(self, name, tool):
        self.m_names.append(name)
        self.m_tools[name] = tool

    def reset(self):
        self.m_names.clear()
        self.m_tools.clear()
