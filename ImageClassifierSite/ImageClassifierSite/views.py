from django.shortcuts import render

from . import Classifier as cls

def index(request):

	if request.method == 'GET':
		return render(request, "index.html")
	if request.method == 'POST':

		# Get picture

		# Upload

		# Run through classifier

		#classifier = cls.Classifier()
		#classifier.classify_image(image)

		# Output result

		# Upload photo to database

		return render(request, "result.html")


