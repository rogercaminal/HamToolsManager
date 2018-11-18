from ContestAnalyzerOnline.contestAnalyzer.plots.plot_base import PlotBase
import plotly.offline as py
import plotly.graph_objs as go


class PlotDbVsDate(PlotBase):

    def __init__(self, name):
        super(PlotDbVsDate, self).__init__(name)

    def do_plot(self, contest, doSave, options=""):

        # --- Define dictionaries
        x = {}
        y = {}

        colors = {}
        colors[10]  = "blue"
        colors[15]  = "orange"
        colors[20]  = "green"
        colors[40]  = "red"
        colors[80]  = "purple"
        colors[160] = "brown"

        # --- Extra conditions
        extra_conditions = (contest.rbspots["db"]>0.)
        avg = "15min"
        band = None
        for opt in options.split(","):
            if "band" in opt:
                band = opt.replace("band", "")+"m"
            if "continent" in opt:
                cont = opt.replace("continent", "")
                extra_conditions &= (contest.rbspots["de_cont"]==cont)
            if "call" in opt:
                call = opt.replace("call", "")
                extra_conditions &= (contest.rbspots["callsign"]==call)
            if "avg" in opt:
                avg = opt.replace("avg", "")

        contest.rbspots["date_round%s"%avg] = contest.rbspots["date"].dt.round(avg)

        # --- Define the datasets
        y[10] = contest.rbspots[(contest.rbspots["band"] == "10m") & extra_conditions].groupby("date_round%s" % avg)["db"].mean()
        y[15] = contest.rbspots[(contest.rbspots["band"] == "15m") & extra_conditions].groupby("date_round%s" % avg)["db"].mean()
        y[20] = contest.rbspots[(contest.rbspots["band"] == "20m") & extra_conditions].groupby("date_round%s" % avg)["db"].mean()
        y[40] = contest.rbspots[(contest.rbspots["band"] == "40m") & extra_conditions].groupby("date_round%s" % avg)["db"].mean()
        y[80] = contest.rbspots[(contest.rbspots["band"] == "80m") & extra_conditions].groupby("date_round%s" % avg)["db"].mean()
        y[160] = contest.rbspots[(contest.rbspots["band"] == "160m") & extra_conditions].groupby("date_round%s" % avg)["db"].mean()
        x[10] = y[10].index.tolist()
        x[15] = y[15].index.tolist()
        x[20] = y[20].index.tolist()
        x[40] = y[40].index.tolist()
        x[80] = y[80].index.tolist()
        x[160] = y[160].index.tolist()

        # --- Define data object
        data = []
        for b in [10, 15, 20, 40, 80, 160]:
            if band is None:
                data.append(go.Scatter(x=x[b] , y=y[b] , line=dict(color=(colors[b]),   width=3), hoverinfo="x+y", mode="lines", name="%dm"%b))
            else:
                if str("%dm"%b)==band:
                    data.append(go.Scatter(x=x[b] , y=y[b] , line=dict(color=(colors[b]),   width=3), hoverinfo="x+y", mode="line", name="%dm"%b))

        layout = go.Layout(
            barmode='stack',
            title='TX signal report vs date %s' % (options),
            xaxis=dict(title="Time", rangeselector=dict(buttons=[dict(count=1, label='1h', step='hour', stepmode='backward'), dict(count=6, label='6h', step='hour', stepmode='backward'), dict(count=12, label='12h', step='hour', stepmode='backward'), dict(count=24, label='24h', step='hour', stepmode='backward'), dict(step='all')]), rangeslider=dict()),
            yaxis=dict(title="dB"),
            width=750,
            height=750,
        )

        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, auto_open=False, output_type='div')
