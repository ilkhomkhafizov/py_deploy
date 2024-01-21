from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.status import HTTP_200_OK
from rest_framework.authentication import BaseAuthentication, SessionAuthentication

from .models import Blog, Post
from .serializers import BlogSerializer, BlogTestSerializer, PostSerializer, PostModelSerializer
from .pagination import StandardResultsSetPagination


class BlogListApiView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostModelViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    # authentication_classes = [BaseAuthentication]
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, renderer_classes=[renderers.JSONRenderer])
    def active(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({"is_active": post.is_active})


class BLogApiView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        blogs_data = BlogTestSerializer(blogs, many=True)
        data = {"blog": blogs_data.data}
        return Response(data, status=HTTP_200_OK)

    def post(self, request):
        serializer = BlogTestSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class PostApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        json_data = PostSerializer(posts, many=True)
        return Response({"posts": json_data.data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Post.objects.get(pk=pk)
        except: # noqa
            return Response({"error": "Object does not exist"})

        serializer = PostSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
