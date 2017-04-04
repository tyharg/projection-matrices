from django import forms
from django.contrib.postgres.forms import SimpleArrayField

class numberForm(forms.Form):
	numbers = SimpleArrayField(forms.FloatField())
	rows = forms.IntegerField()
	cols = forms.IntegerField()

