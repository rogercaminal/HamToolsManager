import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_qsos_vs_time__band(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):
        #--- Plot QSOs per hour and freq
        qsos10 = None
        qsos15 = None
        qsos20 = None
        qsos40 = None
        qsos80 = None
        qsos160 = None
        if options=="":
            qsos10  = contest.log[(contest.log["band"]==10 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
            qsos15  = contest.log[(contest.log["band"]==15 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
            qsos20  = contest.log[(contest.log["band"]==20 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
            qsos40  = contest.log[(contest.log["band"]==40 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
            qsos80  = contest.log[(contest.log["band"]==80 ) & (pd.isnull(contest.log["continent"])==False)]["hour"]
            qsos160 = contest.log[(contest.log["band"]==160) & (pd.isnull(contest.log["continent"])==False)]["hour"]
        elif "continent" in options:
            continent = options
            qsos10  = contest.log[(contest.log["band"]==10 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos15  = contest.log[(contest.log["band"]==15 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos20  = contest.log[(contest.log["band"]==20 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos40  = contest.log[(contest.log["band"]==40 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos80  = contest.log[(contest.log["band"]==80 ) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]
            qsos160 = contest.log[(contest.log["band"]==160) & (pd.isnull(contest.log["continent"])==False) & (contest.log["continent"]==continent)]["hour"]

        x = range(0, 48)
        data = [
                go.Histogram(x=qsos10,  name="10m",  xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos15,  name="15m",  xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos20,  name="20m",  xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos40,  name="40m",  xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos80,  name="80m",  xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos160, name="160m", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                ]

        layout = go.Layout(
            barmode='stack',
            title='QSOs per hour - band',
            xaxis=dict(title="Hour", nticks=24),
            yaxis=dict(title="QSOs"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
