from django.shortcuts import render

from . import forms
from .ImageHandler.classifier import Classifier
from .ImageHandler import file_handler

def index(request):

	def host_image(form):
		""" Saves image to /media/ """
		image = form.save()
		image_path = image.upload.url.strip('/')
		return image_path

	def classify_image(image_path):
		classifier = Classifier()
		return classifier.pipeline(image_path)

	if request.method == "GET":
		return render(request, "index.html", {
			'image_form': forms.ImageForm()
		})

	if request.method == "POST":
		form = forms.ImageForm(request.POST, request.FILES)
		if form.is_valid():
			image_path = host_image(form)
			classification = classify_image(image_path)
			# Change to AJAX
			return render(request, "results.html", {
					'image_path': image_path,
					'color': classification['border']
			})
		else:
			# return errors
			pass

