from django.conf.urls import url
from glasgowgigs import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'artists/', views.artists, name='artists'),
    url(r'venues/', views.venues, name='venues'),
]
