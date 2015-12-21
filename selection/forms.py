from django import forms

class SelectionForm(forms.Form):
	name = forms.CharField(max_length=50)
	netid = forms.CharField(max_length=50)