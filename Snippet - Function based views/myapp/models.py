from django.db import models

# Create your models here.

class Snippet(models.Model):
	title=models.CharField(max_length=100)
	code=models.CharField(max_length=100)
	linenos=models.BooleanField()
	language=models.CharField(max_length=50)
	style=models.CharField(max_length=100)

	def __str__(self):
		return self.title