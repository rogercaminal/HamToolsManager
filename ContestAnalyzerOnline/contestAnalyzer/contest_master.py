import os

class contest(object):
    def __init__(self):
        self.callsign = ""
        self.contest = ""
        self.cat_operator = ""
        self.cat_assisted = ""
        self.cat_band = ""
        self.cat_power = ""
        self.cat_mode = ""
        self.cat_transmitter = ""
        self.category = ""
        self.name = ""
        self.location = ""
        self.operators = []
        self.club = ""
        self.year = ""
        self.log = None

        self.save = False
        self.folderToSave = ""

        self.logName = ""

        self.maxRates = {}

    def __str__(self):
        line = ""
        line += "Call: %s\n" % self.callsign
        line += "Contest: %s\n" % self.contest
        line += "Category operator: %s\n" % self.cat_operator
        line += "Category assisted: %s\n" % self.cat_assisted
        line += "Category band: %s\n" % self.cat_band
        line += "Category power: %s\n" % self.cat_power
        line += "Category mode: %s\n" % self.cat_mode
        line += "Category transmitte: %s\n" % self.cat_transmitter
        line += "Operator name: %s\n" % self.name
        line += "Location: %s\n" % self.location
        line += "Operator(s) call(s): %s\n" % (' '.join(self.operators))
        line += "Club: %s\n" % self.club
        return line 

    def importLog(self, year, mode, callsign, forceCSV=False):
        pass

    def make_plots(self, save):
        pass
