import logging
import os
from StringIO import StringIO
import zipfile
import numpy as np
import pandas as pd
from urllib2 import urlopen


def import_reverse_beacon_spots(contest):
    logging.info("Getting reverse beacon spots")

    # --- Check if formatted pickle file exists and used unless otherwise specified
    if not os.path.exists("%s.pickle" % contest.log_name.replace(".log", "")):

        spots_list = []
        contest_dates = contest.log.groupby("date").groups.keys()
        contest_dates.sort()

        for d in contest_dates:
            date = d.replace("-","")
            try:
                myzipfile = zipfile.ZipFile(StringIO(urlopen("http://reversebeacon.net/raw_data/dl.php?f=%s"%date).read()))
            except:
                logging.error("Problem getting reverse beacon spots")
                return False
            csvfile = [StringIO(myzipfile.read(name)) for name in myzipfile.namelist()]

            sp = pd.read_csv(csvfile[0], keep_default_na=False, dtype={"callsign": np.object,
                                                                       "de_pfx": np.object,
                                                                       "de_cont": np.object,
                                                                       "freq": np.object,
                                                                       "band": np.object,
                                                                       "dx": np.object,
                                                                       "dx_pfx": np.object,
                                                                       "dx_cont": np.object,
                                                                       "mode": np.object,
                                                                       #"db": np.int64,
                                                                       #"speed": np.int64,
                                                                       #"tx_mode": np.objec
                                                                       }
                             )
            sp["date"] = pd.to_datetime(sp["date"])
            sp["freq"] = pd.to_numeric(sp["freq"])
            sp["speed"] = pd.to_numeric(sp["speed"])
            sp["db"] = pd.to_numeric(sp["db"])
            spots_list.append(sp[sp["dx"] == contest.callsign])
        contest.rbspots = pd.concat(spots_list)
        return True
    return True