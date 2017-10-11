from django import forms


def getYearsTuple():
    import ContestAnalyzerOnline.contestAnalyzer.Utils
    listYears = ContestAnalyzerOnline.contestAnalyzer.Utils.getListOfYears("cqww")
    listTuples = list()
    for y in listYears:
        listTuples.append((y, y))
    return list(reversed(listTuples))

#___________________________________________
class ContestForm(forms.Form):
    name     = forms.ChoiceField(label='Contest name', choices=[("cqww", "CQ WW")])
    callsign = forms.CharField(label='Callsign', max_length=100)
    year     = forms.ChoiceField(label='Year', choices=getYearsTuple())
    mode     = forms.ChoiceField(label='Mode', choices=[("cw", "CW"), ("ssb", "SSB")])

##___________________________________________
#class ContestForm(forms.Form):
#    def __init__(self, *args, **kwargs):
#        super(ContestForm, self).__init__(*args, **kwargs)
#        self.fields["name"]     = forms.ChoiceField(label='Contest name', choices=[("cqww", "CQ WW")])
#        self.fields["callsign"] = forms.CharField(label='Callsign', max_length=100)
#        self.fields["year"]     = forms.ChoiceField(label='Year', choices=getYearsTuple())
#        self.fields["mode"]     = forms.ChoiceField(label='Mode', choices=[("cw", "CW"), ("ssb", "SSB")])
