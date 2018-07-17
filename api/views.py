from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
)
from blog.models import Post
from .serializers import (
    PostSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
