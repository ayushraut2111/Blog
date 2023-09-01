from rest_framework.serializers import ModelSerializer
from .models import BlogPost
from rest_framework import serializers

class BlogSerializer(ModelSerializer):
    Author=serializers.CharField(source="Author.username",read_only=True)    # to view the username instead of user number
    class Meta:
        model=BlogPost
        fields=['id','Author','Title','Body','created_at','updated_at']

    def create(self, validated_data):
        validated_data['Author']=self.context['request'].user   # to get the user
        return BlogPost.objects.create(**validated_data)