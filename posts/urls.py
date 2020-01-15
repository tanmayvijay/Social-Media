from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
	path('', views.posts_home, name='posts_home'),
	path('<slug:topic_slug>', views.posts_home, name='posts_by_topic'),
	path('new/', views.new_post_view, name='new_post'),
	path('drafts/', views.draft_posts, name='draft_posts'),
	path('<int:pk>-<slug:slug>/', views.post_detail, name='post_detail'),
	path('<int:pk>-<slug:slug>/edit', views.edit_post, name='edit_post'),


]