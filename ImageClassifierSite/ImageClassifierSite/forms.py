from django import forms
from . import settings, models

class ImageForm(forms.ModelForm):
	class Meta:
		model = models.Image
		fields = ["upload"]
