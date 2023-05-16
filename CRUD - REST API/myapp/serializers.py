from rest_framework import serializers
from .models import Book 

class BookSeriaizer(serializers.ModelSerializer):
	class meta:
		model=Book
		field=("title","author","isbn","publisher")