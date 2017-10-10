import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_mults_vs_qsos(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):
        data = [
                go.Scatter(x=contest.log["qsos_evol_all"], y=contest.log["mults_evol_all"], name="%s"%(contest.callsign), line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="line")
                ]

        layout = go.Layout(
            barmode='stack',
            title='Multipliers vs QSOs',
            xaxis=dict(title="QSOs"),
            yaxis=dict(title="Multipliers"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
