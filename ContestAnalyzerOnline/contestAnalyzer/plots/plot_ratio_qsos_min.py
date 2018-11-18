from ContestAnalyzerOnline.contestAnalyzer.plots.plot_base import PlotBase
import plotly.offline as py
import plotly.graph_objs as go


class PlotRatioQSOsMin(PlotBase):

    def __init__(self, name):
        super(PlotRatioQSOsMin, self).__init__(name)

    def do_plot(self, contest, doSave, options=""):
        qsos_day1 = None
        qsos_day2 = None
        if options == "all":
            qsos_day1 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0])]["datetime"].value_counts().fillna(0)
            qsos_day2 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1])]["datetime"].value_counts().fillna(0)
        elif options == "running":
            qsos_day1 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0]) & (contest.log["station_type"] == "running")]["datetime"].value_counts()
            qsos_day2 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1]) & (contest.log["station_type"] == "running")]["datetime"].value_counts()
        elif options == "inband":
            qsos_day1 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[0]) & (contest.log["station_type"] == "inband")]["datetime"].value_counts()
            qsos_day2 = contest.log[(contest.log["isdupe"]==False) & (contest.log["date"]==contest.log["date"].iloc[-1]) & (contest.log["station_type"] == "inband")]["datetime"].value_counts()

        data = [
                go.Histogram(x=qsos_day2, name="Day 2", xbins=dict(start=1, end=15, size=1), autobinx=False, marker=dict(line=dict(width=1))),
                go.Histogram(x=qsos_day1, name="Day 1", xbins=dict(start=1, end=15, size=1), autobinx=False, marker=dict(line=dict(width=1))),
                ]

        layout = go.Layout(
            barmode='stack',
            title='QSOs per min',
            xaxis=dict(title="QSOs/min", tickvals=range(1, 15)),
            yaxis=dict(title="Number of times"),
            width=750,
            height=750,
#            bargap=0.2
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')

