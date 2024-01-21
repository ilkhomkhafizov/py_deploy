from django.urls import path
from rest_framework import routers
from django.urls import include

from .views import BlogListApiView, BLogApiView, PostApiView, PostModelViewset


router = routers.DefaultRouter()

router.register(r'posts', PostModelViewset, basename='post')

urlpatterns = [
    path("api/v1/blogs/", BlogListApiView.as_view(), name="blog_list"),
    path("api/v1/test/", BLogApiView.as_view(), name="blog_api"),
    # path("api/v1/posts/", PostApiView.as_view(), name="post list"),
    # path("api/v1/post/<int:pk>/", PostApiView.as_view(), name="post update")
    # path("api/v1/posts/", PostModelViewset.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }), name="post viewset list"),
    # path("api/v1/post/<int:pk>/", PostModelViewset.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy'
    # }),
    #     name="post viewset update"),
    # path("api/v1/post/<int:pk>/active/", PostModelViewset.as_view({
    #     'get': 'active',
    # }),
    #     name="post viewset update")
    path("api/v1/", include(router.urls))
]
