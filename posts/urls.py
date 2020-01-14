from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
	path('', views.posts_home, name='posts_home'),
	path('<int:pk>-<slug:slug>/', views.post_detail, name='post_detail'),

]