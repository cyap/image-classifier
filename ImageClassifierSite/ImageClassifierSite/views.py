from django.shortcuts import render

from . import forms
from .ImageHandler.classifier import Classifier
from .ImageHandler import file_handler

def index(request):

	if request.method == "GET":
		return render(request, "index.html", {
		})

	if request.method == "POST":
		image_path = host_image(image_data, location)
		classification = classify_image(image_path)
		return render(request, "result.html")


	def host_image(image_data, location):
		""" Saves image to /media/ """

		# Hash doesn't persist
		file_name = hash(image_data)
		file_handler.save(image_data, file_name, location)
		return os.path.join(location, file_name)

	def classify_image(image_path):
		classifier = Classifier()
		return classifier.pipeline(image_path)
