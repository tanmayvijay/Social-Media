# imports
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy



# view for main homepage
def homepage(request):
	# if user is loggedd in redirect to posts page
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('posts:posts_home'))

	# otherwise show option for login or register
	return render(request, 'homepage.html')