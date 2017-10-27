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
    mode     = forms.ChoiceField(label='Mode', choices=[("cw", "CW"), ("ph", "SSB")])

#___________________________________________
from .models import Post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'email', 'text')
