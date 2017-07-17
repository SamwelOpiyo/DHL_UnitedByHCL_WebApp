from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^messenger$', views.messenger.as_view(), name='messenger'),
]
