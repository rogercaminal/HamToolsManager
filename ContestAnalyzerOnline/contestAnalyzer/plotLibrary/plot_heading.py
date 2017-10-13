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
        counts_running = []
        counts_inband = []
        counts_multi = []
        directions = []
        binsize = 30
        for direction in range(0, 360, binsize):
            directions.append(direction)

            if options=="":
                counts_running.append(contest.log[(contest.log["station_type"]=="running") & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_inband.append(contest.log[(contest.log["station_type"]=="inband") & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_multi.append(contest.log[(contest.log["station_type"]=="multi") & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
            else:
                band = int(options.replace("band", ""))
                counts_running.append(contest.log[(contest.log["band"]==band) & (contest.log["station_type"]=="running") & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_inband.append(contest.log[(contest.log["band"]==band) & (contest.log["station_type"]=="inband") & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())
                counts_multi.append(contest.log[(contest.log["band"]==band) & (contest.log["station_type"]=="multi") & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+binsize))]["heading"].count())

        #--- Fill data and layouts
        data = [
                go.Area(r=counts_running, t=directions, name="Running", hoverinfo="all"),
                go.Area(r=counts_inband, t=directions, name="Inband", hoverinfo="all"),
                go.Area(r=counts_multi, t=directions, name="Multi", hoverinfo="all"),
                ]

        layout = go.Layout(
            title="Heading",
            orientation=270,
            legend=dict(font=(dict(size=16))),
            width=750,
            height=750,
                )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
