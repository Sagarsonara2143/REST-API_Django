from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(generics.ListCreateAPIView):
	queryset=Book.objects.all()
	serializer_class=BookSerializer

class BookDetails(generics.ListUpdateDestroyAPIView):
	queryset=Book
	serializer_class=BookSerializer