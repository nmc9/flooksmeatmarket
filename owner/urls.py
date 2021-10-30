from django.conf.urls import url
from . import views

app_name = 'owner'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^companyInfo', views.companyInfo, name='CompanyInfo'),
    url(r'^updateCompanyInfo$', views.updateCompanyInfo, name='update-company-info'),
    url(r'^updateUser$', views.updateUser, name='update-user'),
    url(r'^(?P<user_id>[0-9]+)/makeEmp/$', views.makeEmployee, name='makeEmployee'),
    url(r'^(?P<user_id>[0-9]+)/removeEmp/$', views.removeEmployee, name='removeEmployee'),
    url(r'^(?P<user_id>[0-9]+)/deactivate/$', views.deactivateUser, name='deactivateUser'),
    url(r'^(?P<user_id>[0-9]+)/reactivate/$', views.reactivateUser, name='reactivate'),

]
