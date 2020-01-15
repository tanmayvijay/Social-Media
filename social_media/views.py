from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy


def homepage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('posts:posts_home'))
	return render(request, 'homepage.html')