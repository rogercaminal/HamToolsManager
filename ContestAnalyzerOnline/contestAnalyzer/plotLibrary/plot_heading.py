import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_heading(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):
        #--- Get counts
        counts_10  = []
        counts_15  = []
        counts_20  = []
        counts_40  = []
        counts_80  = []
        counts_160 = []
        directions = []
        binsize = 10
        for direction in range(0, 360, binsize):
            directions.append(direction)

            if options=="":
                counts_10.append(contest.log[(contest.log["band"]==10) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_15.append(contest.log[(contest.log["band"]==15) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_20.append(contest.log[(contest.log["band"]==20) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_40.append(contest.log[(contest.log["band"]==40) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_80.append(contest.log[(contest.log["band"]==80) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_160.append(contest.log[(contest.log["band"]==160) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
            else:
                time_from = str(options.replace("from", "").split("to")[0])
                time_to   = str(options.replace("from", "").split("to")[1])
                counts_10.append(contest.log[(contest.log["band"]==10) & (contest.log["time"]>=time_from) & (contest.log["time"]<=time_to) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_15.append(contest.log[(contest.log["band"]==15) & (contest.log["time"]>=time_from) & (contest.log["time"]<=time_to) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_20.append(contest.log[(contest.log["band"]==20) & (contest.log["time"]>=time_from) & (contest.log["time"]<=time_to) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_40.append(contest.log[(contest.log["band"]==40) & (contest.log["time"]>=time_from) & (contest.log["time"]<=time_to) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_80.append(contest.log[(contest.log["band"]==80) & (contest.log["time"]>=time_from) & (contest.log["time"]<=time_to) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_160.append(contest.log[(contest.log["band"]==160) & (contest.log["time"]>=time_from) & (contest.log["time"]<=time_to) & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())

        #--- Fill data and layouts
        data = [
                go.Area(r=counts_10,  t=directions, name="10m",  hoverinfo="all"),
                go.Area(r=counts_15,  t=directions, name="15m",  hoverinfo="all"),
                go.Area(r=counts_20,  t=directions, name="20m",  hoverinfo="all"),
                go.Area(r=counts_40,  t=directions, name="40m",  hoverinfo="all"),
                go.Area(r=counts_80,  t=directions, name="80m",  hoverinfo="all"),
                go.Area(r=counts_160, t=directions, name="160m", hoverinfo="all"),
                ]

        layout = go.Layout(
            title="Heading",
            orientation=270,
            legend=dict(font=(dict(size=16))),
            width=750,
            height=750,
            angularaxis=dict(showticklabels=True)
                )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
