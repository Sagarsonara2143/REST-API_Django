from django.urls import path
from . import views

urlpatterns = [
	path('snippets/',views.snippet_list,name='snippet-list'),
	path('snippets/<int:pk>/',views.snippet_detail,name='snippet-detail'),
]
