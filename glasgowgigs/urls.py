from django.conf.urls import url, include
from glasgowgigs import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  #social login
    url(r'^avatar/', include('avatar.urls')), #avatar
    url(r'^like_venue/$', views.like_venue, name='like_venue'),
    url(r'^like_artist/$', views.like_artist, name='like_artist'),
]
