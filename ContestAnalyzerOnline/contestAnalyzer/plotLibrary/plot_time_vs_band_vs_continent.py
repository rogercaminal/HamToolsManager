import os
import ContestAnalyzerOnline.contestAnalyzer.plotBase
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools

class plot_time_vs_band_vs_continent(ContestAnalyzerOnline.contestAnalyzer.plotBase.plotBase):
    def doPlot(self, contest, doSave, options=""):        

        hoursAF_list = contest.log[contest.log["continent"]=="continentAF"]["hour"].values
        hoursAS_list = contest.log[contest.log["continent"]=="continentAS"]["hour"].values
        hoursEU_list = contest.log[contest.log["continent"]=="continentEU"]["hour"].values
        hoursNA_list = contest.log[contest.log["continent"]=="continentNA"]["hour"].values
        hoursSA_list = contest.log[contest.log["continent"]=="continentSA"]["hour"].values
        hoursOC_list = contest.log[contest.log["continent"]=="continentOC"]["hour"].values

        bandsAF_list = contest.log[contest.log["continent"]=="continentAF"]["band_int"].values
        bandsAS_list = contest.log[contest.log["continent"]=="continentAS"]["band_int"].values
        bandsEU_list = contest.log[contest.log["continent"]=="continentEU"]["band_int"].values
        bandsNA_list = contest.log[contest.log["continent"]=="continentNA"]["band_int"].values
        bandsSA_list = contest.log[contest.log["continent"]=="continentSA"]["band_int"].values
        bandsOC_list = contest.log[contest.log["continent"]=="continentOC"]["band_int"].values

        max_AF = contest.log[contest.log["continent"]=="continentAF"].groupby(["hour", "band_int"]).count().max()["call"]
        max_AS = contest.log[contest.log["continent"]=="continentAS"].groupby(["hour", "band_int"]).count().max()["call"]
        max_EU = contest.log[contest.log["continent"]=="continentEU"].groupby(["hour", "band_int"]).count().max()["call"]
        max_NA = contest.log[contest.log["continent"]=="continentNA"].groupby(["hour", "band_int"]).count().max()["call"]
        max_SA = contest.log[contest.log["continent"]=="continentSA"].groupby(["hour", "band_int"]).count().max()["call"]
        max_OC = contest.log[contest.log["continent"]=="continentOC"].groupby(["hour", "band_int"]).count().max()["call"]
        maximum = max(max_AF, max(max_AS, max(max_EU, max(max_NA, max(max_SA, max_OC)))))

        data = [
                go.Histogram2d(x=hoursAF_list, y=bandsAF_list, xbins=dict(start=0, end=48, size=1), ybins=dict(start=1, end=7, size=1), zmin=0, zmax=maximum, hoverinfo="x+y+z"),
                go.Histogram2d(x=hoursAS_list, y=bandsAS_list, xbins=dict(start=0, end=48, size=1), ybins=dict(start=1, end=7, size=1), zmin=0, zmax=maximum, hoverinfo="x+y+z"),
                go.Histogram2d(x=hoursEU_list, y=bandsEU_list, xbins=dict(start=0, end=48, size=1), ybins=dict(start=1, end=7, size=1), zmin=0, zmax=maximum, hoverinfo="x+y+z"),
                go.Histogram2d(x=hoursNA_list, y=bandsNA_list, xbins=dict(start=0, end=48, size=1), ybins=dict(start=1, end=7, size=1), zmin=0, zmax=maximum, hoverinfo="x+y+z"),
                go.Histogram2d(x=hoursSA_list, y=bandsSA_list, xbins=dict(start=0, end=48, size=1), ybins=dict(start=1, end=7, size=1), zmin=0, zmax=maximum, hoverinfo="x+y+z"),
                go.Histogram2d(x=hoursOC_list, y=bandsOC_list, xbins=dict(start=0, end=48, size=1), ybins=dict(start=1, end=7, size=1), zmin=0, zmax=maximum, hoverinfo="x+y+z"),
                ]

        fig = plotly.tools.make_subplots(rows=3, cols=2, subplot_titles=("AF", "AS", "EU", "NA", "SA", "OC"))
        fig.append_trace(data[0], 1, 1)
        fig.append_trace(data[1], 1, 2)
        fig.append_trace(data[2], 2, 1)
        fig.append_trace(data[3], 2, 2)
        fig.append_trace(data[4], 3, 1)
        fig.append_trace(data[5], 3, 2)
        fig["layout"].update(
                title='Band vs time for each continent',
                xaxis1=dict(title="Hour", nticks=24),
                xaxis2=dict(title="Hour", nticks=24),
                xaxis3=dict(title="Hour", nticks=24),
                xaxis4=dict(title="Hour", nticks=24),
                xaxis5=dict(title="Hour", nticks=24),
                xaxis6=dict(title="Hour", nticks=24),
                yaxis1=dict(title="Band", tickmode="array", tickvals=range(1, 7), ticktext=["10m", "15m", "20m", "40m", "80m", "160m"]),
                yaxis2=dict(title="Band", tickmode="array", tickvals=range(1, 7), ticktext=["10m", "15m", "20m", "40m", "80m", "160m"]),
                yaxis3=dict(title="Band", tickmode="array", tickvals=range(1, 7), ticktext=["10m", "15m", "20m", "40m", "80m", "160m"]),
                yaxis4=dict(title="Band", tickmode="array", tickvals=range(1, 7), ticktext=["10m", "15m", "20m", "40m", "80m", "160m"]),
                yaxis5=dict(title="Band", tickmode="array", tickvals=range(1, 7), ticktext=["10m", "15m", "20m", "40m", "80m", "160m"]),
                yaxis6=dict(title="Band", tickmode="array", tickvals=range(1, 7), ticktext=["10m", "15m", "20m", "40m", "80m", "160m"]),
                width=750,
                height=750,
                )

        return py.plot(fig, auto_open=False, output_type='div')
