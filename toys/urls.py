from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^toys/$', views.toy_list),
    url(r'^toy/(?P<pk>[0-9]+)$', views.toy_detail),
]
