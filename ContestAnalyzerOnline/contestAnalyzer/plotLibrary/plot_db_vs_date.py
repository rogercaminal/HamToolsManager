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
        avg = "15min"
        for opt in options.split(","):
            if "continent" in opt:
                cont = opt.replace("continent", "")
                extraConditions &= (contest.rbspots["de_cont"]==cont)
            if "call" in opt:
                call = opt.replace("call", "")
                extraConditions &= (contest.rbspots["callsign"]==call)
            if "avg" in opt:
                avg = opt.replace("avg", "")

        contest.rbspots["date_round%s"%avg] = contest.rbspots["date"].dt.round(avg)

        #--- Define the datasets
        y10  = contest.rbspots[(contest.rbspots["band"]=="10m")  & extraConditions].groupby("date_round%s"%avg)["db"].mean()
        y15  = contest.rbspots[(contest.rbspots["band"]=="15m")  & extraConditions].groupby("date_round%s"%avg)["db"].mean()
        y20  = contest.rbspots[(contest.rbspots["band"]=="20m")  & extraConditions].groupby("date_round%s"%avg)["db"].mean()
        y40  = contest.rbspots[(contest.rbspots["band"]=="40m")  & extraConditions].groupby("date_round%s"%avg)["db"].mean()
        y80  = contest.rbspots[(contest.rbspots["band"]=="80m")  & extraConditions].groupby("date_round%s"%avg)["db"].mean()
        y160 = contest.rbspots[(contest.rbspots["band"]=="160m") & extraConditions].groupby("date_round%s"%avg)["db"].mean()
        x10  = y10.index.tolist()
        x15  = y15.index.tolist()
        x20  = y20.index.tolist()
        x40  = y40.index.tolist()
        x80  = y80.index.tolist()
        x160 = y160.index.tolist()
        data = [
                go.Scatter(x=x10 , y=y10 , line=dict(color=('blue'),   width=3), hoverinfo="x+y", mode="line", name="10m"),
                go.Scatter(x=x15 , y=y15 , line=dict(color=('orange'), width=3), hoverinfo="x+y", mode="line", name="15m"),
                go.Scatter(x=x20 , y=y20 , line=dict(color=('gren'),   width=3), hoverinfo="x+y", mode="line", name="20m"),
                go.Scatter(x=x40 , y=y40 , line=dict(color=('red'),    width=3), hoverinfo="x+y", mode="line", name="40m"),
                go.Scatter(x=x80 , y=y80 , line=dict(color=('purple'), width=3), hoverinfo="x+y", mode="line", name="80m"),
                go.Scatter(x=x160, y=y160, line=dict(color=('brown'),  width=3), hoverinfo="x+y", mode="line", name="160m"),
                ]

        layout = go.Layout(
            barmode='stack',
            title='TX signal report vs date %s' % (options),
            xaxis=dict(title="Time", rangeselector=dict(buttons=[dict(count=1, label='1h', step='hour', stepmode='backward'), dict(count=6, label='6h', step='hour', stepmode='backward'), dict(count=12, label='12h', step='hour', stepmode='backward'), dict(count=24, label='24h', step='hour', stepmode='backward'), dict(step='all')]), rangeslider=dict()),
            yaxis=dict(title="dB"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
