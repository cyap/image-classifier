from django import forms
from . import models

class ImageForm(forms.ModelForm):
	class Meta:
		model = models.Image
		fields = ["upload"]

class WebImageForm(forms.Form):
	url = forms.URLField()