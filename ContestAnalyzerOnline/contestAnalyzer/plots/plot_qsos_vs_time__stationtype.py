from ContestAnalyzerOnline.contestAnalyzer.plots.plot_base import PlotBase
import plotly.offline as py
import plotly.graph_objs as go


class PlotQSOsVsTimeStationtype(PlotBase):

    def __init__(self, name):
        super(PlotQSOsVsTimeStationtype, self).__init__(name)

    def do_plot(self, contest, doSave, options=""):
        qsos_running = contest.log[(contest.log["station_type"]=="running")]["hour"]
        qsos_inband = contest.log[(contest.log["station_type"]=="inband")]["hour"]
        qsos_multi = contest.log[(contest.log["station_type"]=="multi")]["hour"]

        x = range(0, 48)
        data = [
                go.Histogram(x=qsos_running, name="Running", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos_inband,  name="Inband", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos_multi,   name="Multiplier", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                ]

        layout = go.Layout(
            barmode='stack',
            title='QSOs per hour - station type',
            xaxis=dict(title="Hour", nticks=24),
            yaxis=dict(title="QSOs"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
