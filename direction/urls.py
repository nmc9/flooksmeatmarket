from django.conf.urls import url
from . import views

app_name = 'direction'
urlpatterns = [


    url(r'^$', views.index, name='index'),

]
