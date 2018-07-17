from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.post_create, name='create'),
    path('post/<id>/delete', views.post_delete, name='delete'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('post/<slug>', views.post_details, name='post_details'),
]
