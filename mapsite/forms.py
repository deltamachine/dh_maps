from django import forms


class DataForm(forms.Form):
    map_name = forms.CharField(label='map_name', max_length=300)
    data = forms.FileField()