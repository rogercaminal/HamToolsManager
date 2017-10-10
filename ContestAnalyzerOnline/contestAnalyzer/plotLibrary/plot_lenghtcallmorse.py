import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import ContestAnalyzerOnline.contestAnalyzer.morseHelper
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_lenghtcallmorse(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):

        qsos_length  = contest.log["morse_length_seconds"]

        mylength = int(options.replace("WPM", ""))
        mconvert = ContestAnalyzerOnline.contestAnalyzer.morseHelper.morse_converter(mylength)

        mconvert.clean()
        mconvert.setString("test %s %s" % (contest.callsign, contest.callsign))
        time_mycall_long = mconvert.getTime()

        mconvert.clean()
        mconvert.setString("test %s" % (contest.callsign))
        time_mycall_short = mconvert.getTime()

        mconvert.clean()
        mconvert.setString("tu %s" % (contest.callsign))
        time_tu = mconvert.getTime()

        mconvert.clean()
        mconvert.setString("%s 5nn" % (contest.callsign))
        time_rst = mconvert.getTime()

        x = range(0, 48)
        data = [
                go.Histogram(x=qsos_length, name="All", xbins=dict(start=0, end=6, size=0.2), marker=dict(line=dict(width=1))),
                ]

        layout = go.Layout(
            barmode='stack',
            title='Morse call length',
            xaxis=dict(title="Time [s]", nticks=24),
            yaxis=dict(title="# QSOs"),
            width=750,
            height=750,
            annotations=[
                dict(x=time_mycall_long, y=0, xref="x", yref="y", text=str('<b>TEST %s %s @ %d WPM</b>'%(contest.callsign, contest.callsign, mylength)), showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, ax=50, ay=-50,),
                dict(x=time_mycall_short, y=0, xref="x", yref="y", text=str('<b>TEST %s @ %d WPM</b>'%(contest.callsign, mylength)), showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, ax=10, ay=-120,),
                dict(x=time_tu, y=0, xref="x", yref="y", text=str('<b>TU %s @ %d WPM</b>'%(contest.callsign, mylength)), showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, ax=-70, ay=-150,),
                dict(x=time_rst, y=0, xref="x", yref="y", text=str('<b>%s 5NN @ %d WPM</b>'%(contest.callsign, mylength)), showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, ax=90, ay=-90,),
                ]
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
