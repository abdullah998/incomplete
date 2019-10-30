from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from core.models import BlogPost

class BlogPostSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                  mixins.CreateModelMixin):

    serializer_class = serializers.BlogPostSerializer
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        return self.queryset.filter().order_by('created_on')


class ApiFunc(APIView):
    serializer_class = serializers.BlogPostSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            b = BlogPost()
            b.post = serializer.validated_data.get('post')
            b.title = serializer.validated_data.get('title')
            b.save()
            return Response('abcd')
        else:
            return Response(serializer.errors)

class ApiFunc2(APIView):
    serializer_class = serializers.BlogPostSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            b = BlogPost.objects.get(id=serializer.validated_data.get('id'))
            b.post = serializer.validated_data.get('post')
            b.title = serializer.validated_data.get('title')
            b.save()
            return Response('abcd')
        else:
            return Response(serializer.errors)