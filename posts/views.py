from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def posts_home(request):
	posts = Post.published.all()
	return render(request, 'posts/posts_home.html', {'posts':posts})


def post_detail(request, pk, slug):
	post = get_object_or_404(Post, pk=pk)

	return render(request, 'posts/post_detail.html', {'post':post})