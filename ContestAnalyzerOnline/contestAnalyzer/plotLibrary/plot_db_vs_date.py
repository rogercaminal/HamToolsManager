import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_db_vs_date(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):

        #--- Extra conditions
        extraConditions = (contest.rbspots["db"]>0.)
        if "continent" in options:
            cont = options.replace("continent", "")
            extraConditions &= (contest.rbspots["de_cont"]==cont)
        if "call" in options:
            call = options.replace("call", "")
            extraConditions &= (contest.rbspots["callsign"]==call)

        #--- Define the datasets
        data = [
                go.Scatter(x=contest.rbspots["date"], y=contest.rbspots[(contest.rbspots["band"]=="10m") & extraConditions]["db"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="line", name="10m"),
                go.Scatter(x=contest.rbspots["date"], y=contest.rbspots[(contest.rbspots["band"]=="15m") & extraConditions]["db"], line=dict(color=('orange'), width=4), hoverinfo="x+y", mode="line", name="15m"),
                go.Scatter(x=contest.rbspots["date"], y=contest.rbspots[(contest.rbspots["band"]=="20m") & extraConditions]["db"], line=dict(color=('gren'), width=4), hoverinfo="x+y", mode="line", name="20m"),
                go.Scatter(x=contest.rbspots["date"], y=contest.rbspots[(contest.rbspots["band"]=="40m") & extraConditions]["db"], line=dict(color=('red'), width=4), hoverinfo="x+y", mode="line", name="40m"),
                go.Scatter(x=contest.rbspots["date"], y=contest.rbspots[(contest.rbspots["band"]=="80m") & extraConditions]["db"], line=dict(color=('purple'), width=4), hoverinfo="x+y", mode="line", name="80m"),
                go.Scatter(x=contest.rbspots["date"], y=contest.rbspots[(contest.rbspots["band"]=="160m") & extraConditions]["db"], line=dict(color=('brown'), width=4), hoverinfo="x+y", mode="line", name="160m"),
                ]

        layout = go.Layout(
            barmode='stack',
            title='Received signal vs date %s' % (options),
            xaxis=dict(title="Time", rangeselector=dict(buttons=[dict(count=1, label='1h', step='hour', stepmode='backward'), dict(count=6, label='6h', step='hour', stepmode='backward'), dict(count=12, label='12h', step='hour', stepmode='backward'), dict(count=24, label='24h', step='hour', stepmode='backward'), dict(step='all')]), rangeslider=dict()),
            yaxis=dict(title="dB"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
