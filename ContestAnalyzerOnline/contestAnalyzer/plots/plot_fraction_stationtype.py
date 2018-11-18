from ContestAnalyzerOnline.contestAnalyzer.plots.plot_base import PlotBase
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go


class PlotFractionStationtype(PlotBase):

    def __init__(self, name):
        super(PlotFractionStationtype, self).__init__(name)

    def do_plot(self, contest, doSave, options=""):
        #--- Plot QSOs per hour and station type
        qsos_running = contest.log[(contest.log["station_type"] == "running") & (pd.isnull(contest.log["continent"]) == False)]["hour"].count()
        qsos_inband = contest.log[(contest.log["station_type"] == "inband") & (pd.isnull(contest.log["continent"]) == False)]["hour"].count()
        qsos_multi = contest.log[(contest.log["station_type"] == "multi") & (pd.isnull(contest.log["continent"]) == False)]["hour"].count()

        labels = ["Running", "Inband", "Multiplier"]
        values = [qsos_running, qsos_inband, qsos_multi]

        data = [
                go.Pie(values=values, labels=labels, name="Blebleble", hoverinfo="label+percent+value", textinfo="percent")
                ]

        layout = go.Layout(
            title='QSO fraction - Station type',
            width=750,
            height=750,
        )

        fig = dict(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')

