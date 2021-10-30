from django.conf.urls import url
from . import views

app_name = 'product'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<basketAdded>\d+)$', views.index, name='index'),
    url(r'^(?P<searchby>AL|BF|PK|PT|SM|DI|GS|XX)$', views.productSearch, name='product-search'),
    url(r'^(?P<searchby>AL|BF|PK|PT|SM|DI|GS|XX)/(?P<basketAdded>\d+)$', views.productSearch, name='product-search'),
    url(r'^(?P<pk>[0-9]+)/addProduct$', views.productAddBasket, name='addBasket'),
    url(r'add/$', views.ProductAdd.as_view(), name='product-add'),
    url(r'(?P<pk>[0-9]+)/update$', views.ProductUpdate.as_view(), name='product-update'),
    url(r'(?P<pk>[0-9]+)/delete$', views.ProductDelete.as_view(), name='product-delete')

]
