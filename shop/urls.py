from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
      url(r'^$', views.product_list, name='product_list'),
      path('<slug:category_slug>/$', views.product_list, name='product_list_by_category'),
      url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
      url(r'^aboutUs.html/$', views.about, name='about_us'),

]
