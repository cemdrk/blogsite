from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    PostCreateAPIView,
)


urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('<int:pk>', PostDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
]
