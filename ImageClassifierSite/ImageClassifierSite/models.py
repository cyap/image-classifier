from django.db import models

class Image(models.Model):
	upload = models.FileField(upload_to='uploads/')