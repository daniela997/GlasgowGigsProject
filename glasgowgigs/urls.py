from django.conf.urls import url, include
from glasgowgigs import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'artists/', views.artists, name='artists'),
    url(r'venues/', views.venues, name='venues'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  #social login
    url(r'^avatar/', include('avatar.urls')),
]
