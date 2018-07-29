import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_freq_vs_date(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):

    def doPlot(self, contest, doSave, options=""):

        binning = {}
        if contest.cat_mode=="CW":
            binning[10] = list(range(28000, 28160, 40))
            binning[15] = list(range(21000, 21160, 40))
            binning[20] = list(range(14000, 14160, 40))
            binning[40] = list(range(7000, 7100, 25))
            binning[80] = list(range(3500, 3600, 25))
            binning[160] = list(range(1800, 1880, 20))
        if contest.cat_mode=="SSB":
            binning[10] = list(range(28150, 28950, 200))
            binning[15] = list(range(21150, 21450, 75))
            binning[20] = list(range(14150, 14450, 75))
            binning[40] = list(range(7100, 7300, 50))
            binning[80] = list(range(3700, 3900, 50))
            binning[160] = list(range(1800, 2000, 50))

        binning_titles = {}
        for b in binning.keys():
            binning_titles[b] = [ str(s) for s in  binning[b] ]

        width = 0.10

        data = [
                go.Scatter(x=contest.log[(contest.log["station_type"]=="multi")  & (contest.log["band"]==160)]["datetime"],  y=contest.log[(contest.log["station_type"]=="multi") & (contest.log["band"]==160)]["frequency"],  line=dict(color=('red'), width=4), hoverinfo="x+y", mode="markers", name="Multi", xaxis='x', yaxis='y'),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==160)]["datetime"],  y=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==160)]["frequency"],  line=dict(color=('green'), width=4), hoverinfo="x+y", mode="markers", name="Inband", xaxis='x', yaxis='y'),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==160)]["datetime"], y=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==160)]["frequency"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="markers", name="Running", xaxis='x', yaxis='y'),

                go.Scatter(x=contest.log[(contest.log["station_type"]=="multi")  & (contest.log["band"]==80)]["datetime"],  y=contest.log[(contest.log["station_type"]=="multi") & (contest.log["band"]==80)]["frequency"],  line=dict(color=('red'), width=4), hoverinfo="x+y", mode="markers", name="Multi", xaxis='x', yaxis='y2', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==80)]["datetime"],  y=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==80)]["frequency"],  line=dict(color=('green'), width=4), hoverinfo="x+y", mode="markers", name="Inband", xaxis='x', yaxis='y2', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==80)]["datetime"], y=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==80)]["frequency"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="markers", name="Running", xaxis='x', yaxis='y2', showlegend=False),

                go.Scatter(x=contest.log[(contest.log["station_type"]=="multi")  & (contest.log["band"]==40)]["datetime"],  y=contest.log[(contest.log["station_type"]=="multi") & (contest.log["band"]==40)]["frequency"],  line=dict(color=('red'), width=4), hoverinfo="x+y", mode="markers", name="Multi", xaxis='x', yaxis='y3', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==40)]["datetime"],  y=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==40)]["frequency"],  line=dict(color=('green'), width=4), hoverinfo="x+y", mode="markers", name="Inband", xaxis='x', yaxis='y3', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==40)]["datetime"], y=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==40)]["frequency"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="markers", name="Running", xaxis='x', yaxis='y3', showlegend=False),

                go.Scatter(x=contest.log[(contest.log["station_type"]=="multi")  & (contest.log["band"]==20)]["datetime"],  y=contest.log[(contest.log["station_type"]=="multi") & (contest.log["band"]==20)]["frequency"],  line=dict(color=('red'), width=4), hoverinfo="x+y", mode="markers", name="Multi", xaxis='x', yaxis='y4', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==20)]["datetime"],  y=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==20)]["frequency"],  line=dict(color=('green'), width=4), hoverinfo="x+y", mode="markers", name="Inband", xaxis='x', yaxis='y4', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==20)]["datetime"], y=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==20)]["frequency"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="markers", name="Running", xaxis='x', yaxis='y4', showlegend=False),

                go.Scatter(x=contest.log[(contest.log["station_type"]=="multi")  & (contest.log["band"]==15)]["datetime"],  y=contest.log[(contest.log["station_type"]=="multi") & (contest.log["band"]==15)]["frequency"],  line=dict(color=('red'), width=4), hoverinfo="x+y", mode="markers", name="Multi", xaxis='x', yaxis='y5', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==15)]["datetime"],  y=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==15)]["frequency"],  line=dict(color=('green'), width=4), hoverinfo="x+y", mode="markers", name="Inband", xaxis='x', yaxis='y5', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==15)]["datetime"], y=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==15)]["frequency"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="markers", name="Running", xaxis='x', yaxis='y5', showlegend=False),

                go.Scatter(x=contest.log[(contest.log["station_type"]=="multi")  & (contest.log["band"]==10)]["datetime"],  y=contest.log[(contest.log["station_type"]=="multi") & (contest.log["band"]==10)]["frequency"],  line=dict(color=('red'), width=4), hoverinfo="x+y", mode="markers", name="Multi", xaxis='x', yaxis='y6', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==10)]["datetime"],  y=contest.log[(contest.log["station_type"]=="inband") & (contest.log["band"]==10)]["frequency"],  line=dict(color=('green'), width=4), hoverinfo="x+y", mode="markers", name="Inband", xaxis='x', yaxis='y6', showlegend=False),
                go.Scatter(x=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==10)]["datetime"], y=contest.log[(contest.log["station_type"]=="running") & (contest.log["band"]==10)]["frequency"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="markers", name="Running", xaxis='x', yaxis='y6', showlegend=False),
                ]

        layout = go.Layout(
            title='Frequency vs date',
            xaxis=dict(title="Time", rangeselector=dict(buttons=[dict(count=1, label='1h', step='hour', stepmode='backward'), dict(count=6, label='6h', step='hour', stepmode='backward'), dict(count=12, label='12h', step='hour', stepmode='backward'), dict(count=24, label='24h', step='hour', stepmode='backward'), dict(step='all')]), rangeslider=dict(), anchor='x'),
            yaxis=dict(title="160m", tickmode="array", range=[binning[160][0]-1, binning[160][-1]], tickvals=binning[160], ticktext=binning_titles[160], anchor='y', domain=[0, 0.+width]),
            yaxis2=dict(title="80m", tickmode="array", range=[binning[80][0]-1, binning[80][-1]]  , tickvals=binning[80] , ticktext=binning_titles[80] , anchor='y2', domain=[0.167, 0.167+width]),
            yaxis3=dict(title="40m", tickmode="array", range=[binning[40][0]-1, binning[40][-1]]  , tickvals=binning[40] , ticktext=binning_titles[40] , anchor='y3', domain=[0.333, 0.333+width]),
            yaxis4=dict(title="20m", tickmode="array", range=[binning[20][0]-1, binning[20][-1]]  , tickvals=binning[20] , ticktext=binning_titles[20] , anchor='y4', domain=[0.500, 0.500+width]),
            yaxis5=dict(title="15m", tickmode="array", range=[binning[15][0]-1, binning[15][-1]]  , tickvals=binning[15] , ticktext=binning_titles[15] , anchor='y5', domain=[0.667, 0.667+width]),
            yaxis6=dict(title="10m", tickmode="array", range=[binning[10][0]-1, binning[10][-1]]  , tickvals=binning[10] , ticktext=binning_titles[10] , anchor='y6', domain=[0.833, 0.833+width]),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
