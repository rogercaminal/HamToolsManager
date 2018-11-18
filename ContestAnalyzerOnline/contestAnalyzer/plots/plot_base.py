

class PlotBase(object):
    def __init__(self, name):
        self.m_name = name

    def __str__(self):
        return self.m_name

    def do_plot(self, contest, doSave, options=""):
        pass
