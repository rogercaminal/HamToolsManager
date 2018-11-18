from ContestAnalyzerOnline.contestAnalyzer.plots.plot_base import PlotBase
import plotly.offline as py
import plotly.graph_objs as go


class PlotHeading(PlotBase):

    def __init__(self, name):
        super(PlotHeading, self).__init__(name)

    def do_plot(self, contest, doSave, options=""):
        # --- Get counts
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

        # --- Add extra condition to all selections
        extra_conditions = (contest.log["band"]>0)
        band = None
        for opt in options.split(","):
            if "band" in opt:
                band = int(str(opt.replace("band", "")))
            if "from" in opt:
                time_from = str(opt.replace("from", ""))
                extra_conditions &= (contest.log["time"]>=time_from)
            if "to" in opt:
                time_to   = str(opt.replace("to", ""))
                extra_conditions &= (contest.log["time"]<=time_to)

        # --- Loop on bins of direction
        bin_size = 10
        for direction in range(0, 360, bin_size):
            directions.append(direction)

            counts[10].append(contest.log[(contest.log["band"]==10) & extra_conditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+bin_size))]["heading"].count())
            counts[15].append(contest.log[(contest.log["band"]==15) & extra_conditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+bin_size))]["heading"].count())
            counts[20].append(contest.log[(contest.log["band"]==20) & extra_conditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+bin_size))]["heading"].count())
            counts[40].append(contest.log[(contest.log["band"]==40) & extra_conditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+bin_size))]["heading"].count())
            counts[80].append(contest.log[(contest.log["band"]==80) & extra_conditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+bin_size))]["heading"].count())
            counts[160].append(contest.log[(contest.log["band"]==160) & extra_conditions & (contest.log["heading"]>direction) & (contest.log["heading"]<(direction+bin_size))]["heading"].count())

        maximum = 0
        for i in range(len(counts[10])):
            if band is None:
                m = max(counts[10][i], max(counts[15][i], max(counts[20][i], max(counts[40][i], max(counts[80][i], counts[160][i])))))
            else:
                m = counts[band][i]
            if m>maximum:
                maximum = m


        # --- Fill data and layouts
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
