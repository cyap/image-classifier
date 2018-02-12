from urllib.request import urlretrieve, urlopen

from django.shortcuts import render
from django.core.files import File
from django.core.files.base import ContentFile

from . import forms
from .ImageHandler.classifier import Classifier

import os
from . import settings

def index(request):

	def host_image(form):
		""" Saves image to /media/ """
		image = form.save()
		image_path = image.upload.url.strip('/')
		return image_path

	def classify_image(image_path):
		classifier = Classifier()
		return classifier.pipeline(image_path)

	def file_from_url(url):
		content = urlopen(url).read()
		name = url.rsplit('/', 1)[1]
		return {'upload': ContentFile(content, name)}

	if request.method == "GET":
		return render(request, "index.html", {
			'image_form': forms.ImageForm(),
			'web_image_form': forms.WebImageForm()
		})

	if request.method == "POST":
		upload = request.FILES or file_from_url(request.POST['url'])
		form = forms.ImageForm(request.POST, upload)

		if form.is_valid():
			image_path = host_image(form)
			classification = classify_image(os.path.join(settings.BASE_DIR, image_path))

			# Change to AJAX
			return render(request, "results.html", {
					'image_path': image_path,
					'classification': classification
			})
		else:
			return render(request, "index.html", {
				'image_form': forms.ImageForm(),
				'web_image_form': forms.WebImageForm(),
				'error': "Invalid image."
			})
