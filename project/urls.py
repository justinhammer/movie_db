"""project URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url('r^__debug__/', include(debug_toolbar.urls)),

    url(r'^movie_list/', 'main.views.movie_list'),
    url(r'^movie_list_temp/$', 'main.views.movie_list_temp'),
    url(r'^movie_list_mysql/$', 'main.views.movie_list_mysql'),
    url(r'^movie_list_cas/$', 'main.views.movie_list_cas'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)