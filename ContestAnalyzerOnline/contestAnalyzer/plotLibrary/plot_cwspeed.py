import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import ContestAnalyzerOnline.contestAnalyzer.morseHelper
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_cwspeed(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):

        #--- Extra conditions
        extraConditions = (contest.rbspots["speed"]>0.)
        avg = "5min"
        for opt in options.split(","):
            if "band" in opt:
                band = opt.replace("band", "")
                extraConditions &= (contest.rbspots["band"]==str("%sm"%band))
            if "avg" in opt:
                avg = opt.replace("avg", "")

        contest.rbspots["date_round%s"%avg] = contest.rbspots["date"].dt.round(avg)

        #--- Define the datasets
        y  = contest.rbspots[extraConditions].groupby("date_round%s"%avg)["speed"].mean()
        x  = y.index.tolist()
        data = [
                go.Scatter(x=x , y=y , line=dict(color=('blue'),   width=4), hoverinfo="x+y", mode="lines", name="CW speed"),
                ]

        title = 'TX speed vs date'
        if "band" in options:
            title += str(" %sm"%(options.replace("band", "")))

        layout = go.Layout(
            barmode='stack',
            title=title,
            xaxis=dict(title="Time", rangeselector=dict(buttons=[dict(count=1, label='1h', step='hour', stepmode='backward'), dict(count=6, label='6h', step='hour', stepmode='backward'), dict(count=12, label='12h', step='hour', stepmode='backward'), dict(count=24, label='24h', step='hour', stepmode='backward'), dict(step='all')]), rangeslider=dict()),
            yaxis=dict(title="CW speed [WPM]"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
