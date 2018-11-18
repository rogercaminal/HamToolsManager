from ContestAnalyzerOnline.contestAnalyzer.plots.plot_base import PlotBase
import plotly.offline as py
import plotly.graph_objs as go


class PlotQSOsVsTimeContinent(PlotBase):

    def __init__(self, name):
        super(PlotQSOsVsTimeContinent, self).__init__(name)

    def do_plot(self, contest, doSave, options=""):
        qsosEU = contest.log[(contest.log["continent"] == "continentEU")]["hour"]
        qsosNA = contest.log[(contest.log["continent"] == "continentNA")]["hour"]
        qsosSA = contest.log[(contest.log["continent"] == "continentSA")]["hour"]
        qsosAF = contest.log[(contest.log["continent"] == "continentAF")]["hour"]
        qsosOC = contest.log[(contest.log["continent"] == "continentOC")]["hour"]
        qsosAN = contest.log[(contest.log["continent"] == "continentAN")]["hour"]
        qsosAS = contest.log[(contest.log["continent"] == "continentAS")]["hour"]

        x = range(0, 48)
        data = [
                go.Histogram(x=qsosEU, name="EU", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsosNA, name="NA", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsosSA, name="SA", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsosAF, name="AF", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsosOC, name="OC", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsosAN, name="AN", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                go.Histogram(x=qsosAS, name="AS", xbins=dict(start=0, end=48, size=1), marker=dict(line=dict(width=1))),
                ]

        layout = go.Layout(
            barmode='stack',
            title='QSOs per hour - continent',
            xaxis=dict(title="Hour", nticks=24),
            yaxis=dict(title="QSOs"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
