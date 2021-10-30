from django.conf.urls import url
from . import views

app_name = 'contact'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^send$', views.send, name='send'),
]
