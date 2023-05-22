from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
	class meta:
		model=Snippet
		fields=('id','title','code','linenos','language','style')