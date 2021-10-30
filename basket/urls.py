from django.conf.urls import url

from . import views

app_name = 'basket'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.basketDetail, name='detail'),
    url(r'^(?P<user_id>[0-9]+)/(?P<column>Amount|Price|Location)/$', views.basketDetail_column, name='detail-column'),
    url(r'^(?P<user_id>[0-9]+)/edit/$', views.edit, name='edit'),

]
