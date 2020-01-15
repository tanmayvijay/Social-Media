from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

# giving an app name similar to namespace
app_name = 'accounts'

# urls after domain/accounts/
urlpatterns = [
	# path('login', auth_views.LoginView.as_view(), name='login'),
	# accounts home page -- suggested accounts to follow
	path('', views.accounts_home, name='accounts_home'),
	# accounts followed by user
	path('following/', views.following, name='following'),
	# accounts who follow user
	path('followers/', views.followers, name='followers'),
	# logout url
	path('logout', auth_views.LogoutView.as_view(), name='logout'),
	# login page url
	path('login', views.login_view, name='login'),
	# new user registration url
	path('register/', views.register, name='register'),
	# urls to change passwords
	path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	# urls to reset password when forgotten
	path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
	path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
	path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	# url to view profile
	path('<str:username>/', views.profile_view, name='profile'),
	# url to edit self profile
	path('<str:username>/edit', views.edit_profile_view, name='edit_profile'),
	# url to follow a profile
	path('<str:username>/follow', views.follow_view, name='follow'),
	# url to unfollow a profile
	path('<str:username>/unfollow', views.unfollow_view, name='unfollow'),

]

