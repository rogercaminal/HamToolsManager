import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_freq_vs_date(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):
        data = [
                go.Scatter(x=contest.log["datetime"], y=contest.log["frequency"], line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="lines")
                ]

        layout = go.Layout(
            barmode='stack',
            title='Frequency vs date',
            xaxis=dict(title="Time", rangeselector=dict(buttons=[dict(count=1, label='1h', step='hour', stepmode='backward'), dict(count=6, label='6h', step='hour', stepmode='backward'), dict(count=12, label='12h', step='hour', stepmode='backward'), dict(count=24, label='24h', step='hour', stepmode='backward'), dict(step='all')]), rangeslider=dict()),
            yaxis=dict(title="Frequency", tickmode="array", tickvals=range(1000, 30000, 2000), ticktext=["1 MHz", "3 MHz", "5 MHz", "7 MHz", "9 MHz", "11 MHz", "13 MHz", "15 MHz", "17 MHz", "19 MHz", "21 MHz", "23 MHz", "25 MHz", "27 MHz", "29 MHz"]),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
