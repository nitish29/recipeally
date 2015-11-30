"""recipeally URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'recipesearch.views.home', name='home'),
    url(r'^registration/', 'recipeally.views.registration', name='registration'),
    url(r'^login/$', 'recipeally.views.user_login', name='login'),
    url(r'^logout/$', 'recipeally.views.user_logout', name='logout'),
    # url(r'^comments/', 'recipeally.views.comment', name='comment'),
	url(r'^recipe$', 'recipeally.views.recipe', name='recipe'),
	url(r'^search$', 'recipeally.views.search_recipe', name='search'),
    #url('^', include('django.contrib.auth.urls')),
    #url(r'^login/$', 'django.contrib.auth.views.login'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout'),
]