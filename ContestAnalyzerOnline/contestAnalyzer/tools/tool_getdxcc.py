from ContestAnalyzerOnline.contestAnalyzer.tools.tool_base import ToolBase
import numpy as np
from pyhamtools import LookupLib, Callinfo
from pyhamtools.locator import latlong_to_locator, calculate_heading, calculate_heading_longpath, calculate_distance, calculate_distance_longpath

my_lookuplib = LookupLib(lookuptype="countryfile")

class ToolGetDXCC(ToolBase):

    def __init__(self, name):
        super(ToolGetDXCC, self).__init__(name)

    def apply_to_row(self, row):

        cinfo = Callinfo(my_lookuplib)

        #--- Fill columns
        try:
            dxcc = cinfo.get_all(row["call"])
            row["dxcc"]      = dxcc["country"]
            row["zonecq"]    = int(dxcc["cqz"])
            row["zoneitu"]   = int(dxcc["ituz"])
            row["continent"] = "continent"+dxcc["continent"]
            row["latitude"]  = float(dxcc["latitude"])
            row["longitude"] = float(dxcc["longitude"])
            row["locator"]   = latlong_to_locator(dxcc["latitude"], dxcc["longitude"])
        except:
            row["dxcc"]      = np.NaN
            row["zonecq"]    = np.NaN
            row["zoneitu"]   = np.NaN
            row["continent"] = np.NaN
            row["latitude"]  = np.NaN
            row["longitude"] = np.NaN
            row["locator"]   = np.NaN
        return row


    def apply_to_all(self, contest):

        cinfo = Callinfo(my_lookuplib)

        #--- Set correct format
        contest.log["zonecq"]  = contest.log["zonecq"].fillna(-1).astype("int")
        contest.log["zoneitu"] = contest.log["zoneitu"].fillna(-1).astype("int")

        #--- Add information about home call
        dxcc = {}
        try:
            dxcc = cinfo.get_all(contest.callsign)
        except:
            print("Problem getting my own DXCC info!")

        if len(dxcc.keys())>0:
            contest.log["mydxcc"]        = dxcc["country"]
            contest.log["myzonecq"]      = int(dxcc["cqz"])
            contest.log["myzoneitu"]     = int(dxcc["ituz"])
            contest.log["mycontinent"]   = "continent"+dxcc["continent"]
            contest.log["mylatitude"]    = float(dxcc["latitude"])
            contest.log["mylongitude"]   = float(dxcc["longitude"])
            contest.log["mylocator"]     = latlong_to_locator(float(dxcc["latitude"]), float(dxcc["longitude"]))
            contest.log["heading"]       = contest.log.apply(lambda row: calculate_heading(row["mylocator"], row["locator"]) if isinstance(row["locator"], str) else np.NaN, axis=1)
            contest.log["heading_long"]  = contest.log.apply(lambda row: calculate_heading_longpath(row["mylocator"], row["locator"]) if isinstance(row["locator"], str) else np.NaN, axis=1)
            contest.log["distance"]      = contest.log.apply(lambda row: calculate_distance(row["mylocator"], row["locator"]) if isinstance(row["locator"], str) else np.NaN, axis=1)
            contest.log["distance_long"] = contest.log.apply(lambda row: calculate_distance_longpath(row["mylocator"], row["locator"]) if isinstance(row["locator"], str) else np.NaN, axis=1)
        else:
            contest.log["mydxcc"]        = np.NaN
            contest.log["myzonecq"]      = np.NaN
            contest.log["myzoneitu"]     = np.NaN
            contest.log["mycontinent"]   = np.NaN
            contest.log["mylatitude"]    = np.NaN
            contest.log["mylongitude"]   = np.NaN
            contest.log["mylocator"]     = np.NaN
            contest.log["heading"]       = np.NaN
            contest.log["heading_long"]  = np.NaN
            contest.log["distance"]      = np.NaN
            contest.log["distance_long"] = np.NaN
