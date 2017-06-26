from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^login/', views.auth_login, name="authentication"),
	url(r'^$', views.ProductList.as_view(), name='hello'),
	url(r'^logout$', auth_views.logout, {'next_page':'/'}, name=
		'logout'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail'),
	#url(r'^product/new', views.new_product, name='new-product'),
	url(r'^product/new', views.NewProduct.as_view(), name='newproduct'),
	#url(r'^product/update/(?P<pk>\d+)/$', views.UpdateProduct.as_view(), name='deleteproduct'),
]