from django.conf.urls import url

from track.views import dashboard

urlpatterns = [
    url(r'^$', dashboard, name='track-dashboard'),
]
