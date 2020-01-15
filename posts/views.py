from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NewPostForm, EditPostForm
from django.urls import reverse_lazy
from taggit.models import Tag
# Create your views here.
def posts_home(request, topic_slug=None):
	object_list = Post.published.all()

	topic = None
	if topic_slug:
		topic = get_object_or_404(Tag, slug=topic_slug)
		object_list = object_list.filter(topics__in=[topic])

	paginator = Paginator(object_list, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'posts/posts_home.html', {'posts':posts, 'page': page, 'topic':topic})


def post_detail(request, pk, slug):
	post = get_object_or_404(Post, pk=pk)

	return render(request, 'posts/post_detail.html', {'post':post})




def new_post_view(request):
	if request.method =='POST':
		new_post_form = NewPostForm(request.POST)

		if new_post_form.is_valid():
			new_post = new_post_form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			topics = new_post_form.cleaned_data['topics']
			new_post.topics.add(*topics)

			new_post.save()


			
			return render(request, 'posts/draft_post.html', {'new_post':new_post})

	else:
		new_post_form = NewPostForm()

	return render(request, 'posts/new_post.html', {'new_post_form':new_post_form})



def edit_post(request, pk, slug):
	post = get_object_or_404(Post, pk=pk)
	if not request.user == post.author:
		return HttpResponseRedirect(reverse_lazy('posts:post_detail', args=[pk, slug]))
	
	if request.method =='POST':
		edit_post_form = EditPostForm(request.POST)

		if edit_post_form.is_valid():
			cd = edit_post_form.cleaned_data
			post.title = cd['title']
			post.body = cd['body']
			post.topics = cd['topics']
			post.save()

			if post.status == 'draft':
				return render(request, 'posts/draft_post.html', {'new_post':post})
			else:
				return HttpResponseRedirect(reverse_lazy('posts:post_detail', args=[post.pk, post.slug]))

	else:
		edit_post_form = EditPostForm(data={'title': post.title,
								'body': post.body,
								'topics':[]})

	return render(request, 'posts/edit_post.html', {'edit_post_form':edit_post_form})


def draft_posts(request):
	object_list = Post.drafts.filter(author=request.user)
	paginator = Paginator(object_list, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'posts/draft_posts.html', {'posts':posts, 'page': page})
