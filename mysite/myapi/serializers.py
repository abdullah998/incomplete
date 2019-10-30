from rest_framework import serializers
from core.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=('id','post','title','created_on','edited_on')

    id=serializers.CharField(max_length=10)
    post=serializers.CharField(max_length=1024)
    title=serializers.CharField(max_length=128)