from django.conf.urls import url
from . import views

urlpatterns = [
	#TRANSAKSI MASUK
	url(r'^tambah-transaksi-masuk/$', views.TambahTransaksiMasuk, name='tambah-transaksi-masuk'),
	url(r'^$', views.TransaksiMasukViews, name='transaksi-masuk'),
	url(r'^detail-transaksi-masuk/(?P<pk>[0-9]+)$', views.DetailTransaksiMasuk, name='detail-transaksi-masuk'),
	url(r'^edit-transaksi-masuk/(?P<pk>[0-9]+)$', views.EditTransaksiMasuk, name='edit-transaksi-masuk'),
	url(r'^delete-transaksi-masuk/(?P<pk>[0-9]+)$', views.DeleteTransaksiMasuk, name='delete-transaksi-masuk'),
	#TRANSAKSI KELUAR
	url(r'^tambah-transaksi-kaluar/$', views.TambahTransaksiKeluar, name='tambah-transaksi-kaluar'),
	url(r'^transaksi-keluar/$', views.TransaksiKeluarViews, name='transaksi-kaluar'),
	url(r'^detail-transaksi-kaluar/(?P<pk>[0-9]+)$', views.DetailTransaksiKeluar, name='detail-transaksi-kaluar'),
	url(r'^edit-transaksi-kaluar/(?P<pk>[0-9]+)$', views.EditTransaksiKeluar, name='edit-transaksi-kaluar'),
	url(r'^delete-transaksi-kaluar/(?P<pk>[0-9]+)$', views.DeleteTransaksiKeluar, name='delete-transaksi-kaluar'),
]