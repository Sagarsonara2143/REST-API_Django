from django.db import models

# Create your models here.

class Student(models.Model):
	fname=models.CharField(max_length=100,blank=True)
	lname=models.CharField(max_length=100,blank=True)
	email=models.EmailField(max_length=100)
	mobile=models.PositiveIntegerField()
	address=models.CharField(max_length=100,blank=True)
	course=models.CharField(max_length=100,blank=True)
	fees=models.PositiveIntegerField()

	def __str__(self):
		return self.fname+" "+ self.lname