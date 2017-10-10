import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_fraction_stationtype(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):
        #--- Plot QSOs per hour and station type
        qsos_running  = contest.log[(contest.log["station_type"]=="running") & (pd.isnull(contest.log["continent"])==False)]["hour"].count()
        qsos_inband   = contest.log[(contest.log["station_type"]=="inband")  & (pd.isnull(contest.log["continent"])==False)]["hour"].count()
        qsos_multi    = contest.log[(contest.log["station_type"]=="multi")   & (pd.isnull(contest.log["continent"])==False)]["hour"].count()

        labels = ["Running", "Inband", "Multiplier"]
        values = [qsos_running, qsos_inband, qsos_multi]

        data = [
                go.Pie(values=values, labels=labels, name="Blebleble", hoverinfo="label+percent+value", textinfo="percent")
                ]

        layout = go.Layout(
            title='QSO fraction - Station type',
            width=750,
            height=750,
        )

        fig = dict(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')

