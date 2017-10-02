import os
import ContestAnalyzerOnline.contestAnalyzer.toolBase
import pandas as pd
import numpy as np
import ContestAnalyzerOnline.contestAnalyzer.ctydat

ctyfile = open("ContestAnalyzerOnline/contestAnalyzer/cty.dat")
ctydat = ContestAnalyzerOnline.contestAnalyzer.ctydat.CtyDat(ctyfile.readlines())
ctyfile.close()

class tool_getdxcc(ContestAnalyzerOnline.contestAnalyzer.toolBase.toolBase):
    def applyToRow(self, row):
        try:
            dxcc = ctydat.getdxcc(row["call"])
            row["dxcc"]      = dxcc["name"]
            row["zonecq"]    = dxcc["cq"]
            row["zoneitu"]   = dxcc["itu"]
            row["continent"] = "continent"+dxcc["cont"]
            row["latitude"]  = dxcc["lat"]
            row["longitude"] = dxcc["lon"]
            row["prefix"]    = dxcc["prefix"]
        except:
            row["dxcc"]      = np.NaN
            row["zonecq"]    = np.NaN
            row["zoneitu"]   = np.NaN
            row["continent"] = np.NaN
            row["latitude"]  = np.NaN
            row["longitude"] = np.NaN
            row["prefix"]    = np.NaN
        return row

    def applyToAll(self, contest):
        contest.log["zonecq"]  = contest.log["zonecq"].fillna(-1).astype("int")
        contest.log["zoneitu"] = contest.log["zoneitu"].fillna(-1).astype("int")
