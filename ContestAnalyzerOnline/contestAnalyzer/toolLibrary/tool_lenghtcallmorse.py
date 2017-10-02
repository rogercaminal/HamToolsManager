import os
import ContestAnalyzerOnline.contestAnalyzer.toolBase
import pandas as pd
import numpy as np
import ContestAnalyzerOnline.contestAnalyzer.morseHelper

class tool_lenghtcallmorse(ContestAnalyzerOnline.contestAnalyzer.toolBase.toolBase):
    def applyToRow(self, row):
        mconvert = ContestAnalyzerOnline.contestAnalyzer.morseHelper.morse_converter(30)
        mconvert.setString(row["call"])
        time = mconvert.getTime()
        row["morse_length_seconds"] = time
        return row
