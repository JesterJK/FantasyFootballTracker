"""nfl_game_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from teamtrack.views import IndexView, WeekPickView, LoginView, logout, RegisterView, SeePickView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^week/(?P<week>[0-9]+)/$', login_required(WeekPickView.as_view()), name='weekpick'),
    url(r'^see_picks/(?P<week>[0-9]+)/$', login_required(SeePickView.as_view()), name='seepicks'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', logout, name='logout'),
]
