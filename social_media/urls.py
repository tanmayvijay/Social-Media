"""social_media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# imports
from django.contrib import admin
from django.urls import path, include
from . import views as main_views


# list of urls after domain/
urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),
     # website homepage
    path('', main_views.homepage, name='homepage'),
    # accounts app urls
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # posts app urls
    path('posts/', include('posts.urls', namespace='posts')),
]
