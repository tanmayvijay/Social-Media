from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
	path('', views.posts_home, name='posts_home'),
	path('new/', views.new_post, name='new_post'),
	path('<int:pk>-<slug:slug>/', views.post_detail, name='post_detail'),
	path('<int:pk>-<slug:slug>/edit', views.edit_post, name='edit_post'),,


]