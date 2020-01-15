# imports
from django.urls import path
from . import views

# giving app name to identify urls
app_name = 'posts'


# list of urls after domain/posts/
urlpatterns = [
	# posts home page
	path('', views.posts_home, name='posts_home'),
	# to view all topics
	path('topics/', views.topics_view, name='topics_view'),
	# to view posts of specific topic
	path('topics/<slug:topic_slug>', views.posts_home, name='posts_by_topic'),
	# to create a new post
	path('new/', views.new_post_view, name='new_post'),
	# to review draft posts of user (only self)
	path('drafts/', views.draft_posts, name='draft_posts'),
	# to view a post
	path('<int:pk>-<slug:slug>/', views.post_detail, name='post_detail'),
	# to edit a self post
	path('<int:pk>-<slug:slug>/edit', views.edit_post, name='edit_post'),


]