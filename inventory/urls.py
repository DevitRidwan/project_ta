from django.conf.urls import url
from . import views

urlpatterns = [
	#ITEM
	url(r'^tambah-item/$', views.TambahItem, name='tambah-item'),
	url(r'^$', views.ItemViews, name='items'),
	url(r'^detail-item/(?P<pk>[0-9]+)$', views.DetailItem, name='detail-item'),
	url(r'^edit-item/(?P<pk>[0-9]+)$', views.EditItem, name='edit-item'),
	url(r'^delete-item/(?P<pk>[0-9]+)$', views.DeleteItem, name='delete-item'),
	#KATEGORI ITEM
	url(r'^tambah-kategori-item/$', views.TambahKategoriItem, name='tambah-kategori-item'),
	url(r'^kategori-item/$', views.KategoriItemView, name='kategori-item'),
	url(r'^detail-kategori-item/(?P<pk>[0-9]+)$', views.DetailKategoriItem, name='detail-kategori-item'),
	url(r'^edit-kategori-item/(?P<pk>[0-9]+)$', views.EditKategoriItem, name='edit-kategori-item'),
	url(r'^delete-kategori-item/(?P<pk>[0-9]+)$', views.DeleteKategoriItem, name='delete-kategori-item'),
	#MENU
	url(r'^tambah-menu/$', views.TambahMenu, name='tambah-menu'),
	url(r'^menu/$', views.MenuViews, name='menu'),
	#url(r'^detail-menu/(?P<pk>[0-9]+)$', views.DetailKategoriItem, name='detail-kategori-item'),
	url(r'^edit-menu/(?P<pk>[0-9]+)$', views.EditMenu, name='edit-menu'),
	url(r'^delete-menu/(?P<pk>[0-9]+)$', views.DeleteMenu, name='delete-menu'),
]