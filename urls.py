from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^basket/', include('basket.urls')),
    url(r'^product/', include('product.urls')),

]
