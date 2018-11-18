from ContestAnalyzerOnline.contestAnalyzer.tools.tool_base import ToolBase
import numpy as np

class ToolStationType(ToolBase):

    def __init__(self, name):
        super(ToolStationType, self).__init__(name)

    def apply_to_all(self, contest):

        # Count QSOs per frequency to identify runnings
        contest.log["frequency_counts"] = 0
        contest.log["frequency_counts"] = contest.log.groupby(["frequency", "hour"])["frequency"].transform("count")

        # Running threshold (number of QSOs in a frequency in all contest to be considered running)
        threshold = 15

        # Booleans for running and inband
        condition_running = (contest.log['frequency_counts']>threshold)

        condition_inband = ((contest.log['frequency_counts']<threshold) & ( (contest.log['band_int']==contest.log['band_int'].shift(1)) & (contest.log['frequency_counts'].shift(1)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(2)) & (contest.log['frequency_counts'].shift(2)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(3)) & (contest.log['frequency_counts'].shift(3)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(4)) & (contest.log['frequency_counts'].shift(4)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(5)) & (contest.log['frequency_counts'].shift(5)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(6)) & (contest.log['frequency_counts'].shift(6)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(7)) & (contest.log['frequency_counts'].shift(7)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(8)) & (contest.log['frequency_counts'].shift(8)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(9)) & (contest.log['frequency_counts'].shift(9)>threshold) \
                                                                          | (contest.log['band_int']==contest.log['band_int'].shift(10)) & (contest.log['frequency_counts'].shift(10)>threshold)))

        # Final variable
        contest.log["station_type"] = np.where(condition_running, "running",
                                      np.where(condition_inband, "inband",
                                      "multi"
            ))

