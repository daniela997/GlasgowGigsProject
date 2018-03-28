"""glasgowgigs_project URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from glasgowgigs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^glasgowgigs/', include('glasgowgigs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about, name='about'),
    url(r'^artists/', views.ArtistListView.as_view(), name='artists'),
    url(r'^venues/', views.VenueListView.as_view(), name='venues'),
    url(r'^events/', views.EventListView.as_view(), name='events'),
    url(r'^artist/(?P<slug>[-\w]+)/$', views.ArtistDetailView.as_view(), name='artist-detail'),
    url(r'^venue/(?P<slug>[-\w]+)/$', views.VenueDetailView.as_view(), name='venue-detail'),
    url(r'^event/(?P<slug>[-\w]+)/$', views.EventDetailView.as_view(), name='event-detail'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
    url(r'^search-submit/$', views.SearchSubmitView.as_view(), name='search-submit'),
    url(r'^search-results/$', views.SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),
    url(r'^terms-and-conditions/$', views.TermsAndConditions, name='terms-and-conditions'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

