import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_qsos_vs_time__stationtype(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):
        qsos_running  = contest.log[(contest.log["station_type"]=="running")]["hour"]
        qsos_inband   = contest.log[(contest.log["station_type"]=="inband")]["hour"]
        qsos_multi    = contest.log[(contest.log["station_type"]=="multi")]["hour"]

        x = range(0, 48)
        data = [
                go.Histogram(x=qsos_running, name="Running", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos_inband,  name="Inband", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos_multi,   name="Multiplier", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                ]

        layout = go.Layout(
            barmode='stack',
            title='QSOs per hour - station type',
            xaxis=dict(title="Hour", nticks=24),
            yaxis=dict(title="QSOs"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
