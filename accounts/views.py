# imports
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm, LoginForm, EditProfileForm
from .models import UserProfile
# from django.db.models import Q

# Create your views here.

# new user registration view
def register(request):
	# logout required for registration
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('homepage'))

	# if form filled
	if request.method == 'POST':
		user_form = UserRegistrationForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			new_user = user_form.save(commit=False)
			new_profile = profile_form.save(commit=False)

			new_user.set_password(user_form.cleaned_data['password1'])
			new_user.save()

			new_profile.user = new_user
			new_profile.save()

			# login

			return HttpResponse("Success refister!")
	# if new form to be rendered
	else:
		user_form = UserRegistrationForm()
		profile_form = UserProfileForm()


	return render(request, 'accounts/register.html', context={'user_form':user_form, 'profile_form': profile_form})



# login view
def login_view(request):
	# logout required for login
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('homepage'))

	# if form filled
	if request.method == 'POST':
		login_form = LoginForm(data=request.POST)

		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])


			if user is not None:
				if user.is_active:
					login(request, user)
					next_page = request.GET.get('next')

					if next_page:
						return HttpResponseRedirect(next_page)

					return HttpResponseRedirect(reverse_lazy('homepage'))

				else:
					return HttpResponse("Account Terminated!")

			else:
				return HttpResponse("User Doesnt exist!")

	# if new form is to be rendered
	else:
		login_form = LoginForm()


	return render(request, 'accounts/login.html', context={'login_form': login_form})


# view someone's profile
@login_required
def profile_view(request, username):

	user = get_object_or_404(User, username=username)

	# check if the current user follows this user
	follow = False
	try:
		if request.user.profile.following.get(user=user):
			follow = True
	except Exception as e:
		print(e)
	
	return render(request, 'accounts/profile_page.html', {'user': user, 'follow': follow})



# view to edit self profile
@login_required
def edit_profile_view(request, username):
	# to handle attempts to edit someone else's profile
	if not username == request.user.username:
		return HttpResponseRedirect(reverse_lazy('accounts:profile', args=[username]))

	# if form already filled
	if request.method == 'POST':
		edit_form = EditProfileForm(data=request.POST)
		if edit_form.is_valid():
			cd = edit_form.cleaned_data
			user = request.user
			user.first_name = cd['first_name']
			user.last_name = cd['last_name']
			user.email = cd['email']
			user.username = cd['username']

			user.profile.mob_no = cd['mob_no']
			user.profile.save()

			user.save()

			return HttpResponseRedirect(reverse_lazy('accounts:profile', kwargs={'username': user.username}))
	# if form not already filled
	else:
		edit_form = EditProfileForm()

	return render(request, 'accounts/edit_profile.html', {'edit_form':edit_form})
	


# view to follow someone
@login_required
def follow_view(request, username):
	# to prevent following self
	if username == request.user.username:
		return HttpResponseRedirect(reverse_lazy('accounts:profile', args=[username]))


	user_to_follow = get_object_or_404(User, username=username)
	current_user = request.user	

	current_user.profile.following.add(user_to_follow.profile)

	current_user.save()

	return HttpResponseRedirect(reverse_lazy('accounts:profile', kwargs={'username': username}))



# view to unfollow someone
@login_required
def unfollow_view(request, username):
	# to prevent unfollowing self
	if username == request.user.username:
		return HttpResponseRedirect(reverse_lazy('accounts:profile', args=[username]))

		
	user_to_unfollow = get_object_or_404(User, username=username)
	current_user = request.user

	try:
		if current_user.profile.following.get(user=user_to_unfollow):
			current_user.profile.following.remove(user_to_unfollow.profile)
			current_user.save()
	except Exception as e:
		print(e)

	return HttpResponseRedirect(reverse_lazy('accounts:profile', kwargs={'username': username}))




# showing suggested people to follow
@login_required
def accounts_home(request):

	suggested_users = User.objects.exclude(profile__followers__user__username__contains=request.user.username)
	users = request.user.profile.following.all()

	users = User.objects.filter(profile__following__user__username__contains=request.user.username)

	type_of_users = "Suggested Users"
	

	
	return render(request, 'accounts/home.html', {'users': suggested_users, 'type_of_users':type_of_users})




# showing followers
@login_required
def followers(request):

	follower_users = User.objects.filter(profile__following__user__username__contains=request.user.username)

	type_of_users = "Followers"
	

	
	return render(request, 'accounts/home.html', {'users': follower_users, 'type_of_users':type_of_users})





# showing followed people
@login_required
def following(request):

	following_users = request.user.profile.following.all()

	type_of_users = "Following"
	
	return render(request, 'accounts/home.html', {'users': following_users, 'type_of_users':type_of_users})