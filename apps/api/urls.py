"""tgApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from apps.api.views import EntertainerList, EntertainerDetail, EntertainerUpdate, EntertainerDelete
from apps.api.views import VenueList, VenueDetail, VenueUpdate, VenueDelete
from apps.api.views import EventList, EventDetail, EventUpdate, EventDelete
from django.conf.urls import url

urlpatterns = [
    url(r'^entertainers/$', EntertainerList.as_view(), name='entertainer-list'),
    url(r'^entertainer/(?P<id>[0-9]+)/$', EntertainerDetail.as_view(), name='entertainer-detail'),
    url(r'^entertainer/(?P<id>[0-9]+)/update/$', EntertainerUpdate.as_view(), name='entertainer-update'),
    url(r'^entertainer/(?P<id>[0-9]+)/delete/$', EntertainerDelete.as_view(), name='entertainer-delete'),

    url(r'^venues/$', VenueList.as_view(), name='venue-list'),
    url(r'^venue/(?P<id>[0-9]+)/$', VenueDetail.as_view(), name='venue-detail'),
    url(r'^venue/(?P<id>[0-9]+)/update/$', VenueUpdate.as_view(), name='venue-update'),
    url(r'^venue/(?P<id>[0-9]+)/delete/$', VenueDelete.as_view(), name='venue-delete'),

    url(r'^events/$', EventList.as_view(), name='event-list'),
    url(r'^event/(?P<id>[0-9]+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^event/(?P<id>[0-9]+)/update/$', EventUpdate.as_view(), name='event-update'),
    url(r'^event/(?P<id>[0-9]+)/delete/$', EventDelete.as_view(), name='event-delete')
]