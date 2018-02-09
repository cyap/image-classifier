from django import forms
from . import models
from django.core.exceptions import ValidationError
import PIL

class ImageForm(forms.ModelForm):
	class Meta:
		model = models.Image
		fields = ["upload"]

	def clean(self):
		data = super().clean()
		try:
			test = PIL.Image.open(data['upload'].file)
		except:
			raise ValidationError("Cannot be converted to valid PIL image type.")
		return data

class WebImageForm(forms.Form):
	url = forms.URLField()