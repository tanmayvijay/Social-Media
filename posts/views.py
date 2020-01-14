from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def posts_home(request):
	object_list = Post.published.all()
	paginator = Paginator(object_list, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'posts/posts_home.html', {'posts':posts, 'page': page})


def post_detail(request, pk, slug):
	post = get_object_or_404(Post, pk=pk)

	return render(request, 'posts/post_detail.html', {'post':post})




def new_post(request):
	pass


def edit_post(request):
	pass