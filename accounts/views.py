from django.shortcuts import render, HttpResponse
from .forms import UserRegistrationForm, UserProfileForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def register(request):

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
	else:
		user_form = UserRegistrationForm()
		profile_form = UserProfileForm()


	return render(request, 'accounts/register.html', context={'user_form':user_form, 'profile_form': profile_form})


def login_view(request):
	if request.method == 'POST':
		login_form = LoginForm(data=request.POST)

		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])


			if user is not None:
				if user.is_active:
					login(request, user)

					return HttpResponse("Success login!")

				else:
					return HttpResponse("Account Terminated!")

			else:
				return HttpResponse("User Doesnt exist!")

	else:
		login_form = LoginForm()


	return render(request, 'accounts/login.html', context={'login_form': login_form})


