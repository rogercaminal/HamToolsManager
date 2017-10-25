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
        directions = []

        counts = {}
        counts[10]  = []
        counts[15]  = []
        counts[20]  = []
        counts[40]  = []
        counts[80]  = []
        counts[160] = []

        colors = {}
        colors[10]  = "blue"
        colors[15]  = "orange"
        colors[20]  = "green"
        colors[40]  = "red"
        colors[80]  = "purple"
        colors[160] = "brown"

        #--- Add extra condition to all selections
        extraConditions = (contest.log["band"]>0)
        band = None
        for opt in options.split(","):
            if "band" in opt:
                band = int(str(opt.replace("band", "")))
            if "from" in opt:
                time_from = str(opt.replace("from", ""))
                extraConditions &= (contest.log["time"]>=time_from)
            if "to" in opt:
                time_to   = str(opt.replace("to", ""))
                extraConditions &= (contest.log["time"]<=time_to)

        #--- Loop on bins of direction
        binsize = 10
        for direction in range(0, 360, binsize):
            directions.append(direction)

            counts[10].append(contest.log[(contest.log["band"]==10) & extraConditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
            counts[15].append(contest.log[(contest.log["band"]==15) & extraConditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
            counts[20].append(contest.log[(contest.log["band"]==20) & extraConditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
            counts[40].append(contest.log[(contest.log["band"]==40) & extraConditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
            counts[80].append(contest.log[(contest.log["band"]==80) & extraConditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
            counts[160].append(contest.log[(contest.log["band"]==160) & extraConditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())

        maximum = 0
        for i in range(len(counts[10])):
            if band is None:
                m = max(counts[10][i], max(counts[15][i], max(counts[20][i], max(counts[40][i], max(counts[80][i], counts[160][i])))))
            else:
                m = counts[band][i]
            if m>maximum:
                maximum = m


        #--- Fill data and layouts
        bands = [10, 15, 20, 40, 80, 160]
        if band is not None:
            bands = [band]

        data = []
        for b in bands:
            data.append(go.Area(r=counts[b],  t=directions, name="%dm"%b,  hoverinfo="all", marker=dict(color=colors[b])))

        layout = go.Layout(
            title="Beam heading",
            orientation=270,
            legend=dict(font=(dict(size=16))),
            width=750,
            height=750,
            angularaxis=dict(showticklabels=True),
            radialaxis=dict(range=[0,1.2*maximum]),
                )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
