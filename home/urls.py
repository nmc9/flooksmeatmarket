from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^FAQ/$', views.FAQ, name='FAQ')
]

