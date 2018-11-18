from ContestAnalyzerOnline.contestAnalyzer.plots.plot_base import PlotBase
import plotly.offline as py
import plotly.graph_objs as go


class PlotMultsVsQSOs(PlotBase):

    def __init__(self, name):
        super(PlotMultsVsQSOs, self).__init__(name)

    def do_plot(self, contest, doSave, options=""):
        data = [
                go.Scatter(x=contest.log["qsos_evol_all"], y=contest.log["mults_evol_all"], name="%s"%(contest.callsign), line=dict(color=('blue'), width=4), hoverinfo="x+y", mode="lines")
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
