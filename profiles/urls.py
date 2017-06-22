from django.conf.urls import url
from . import views

urlpatterns = [
	#PROFILE
	url(r'^tambah-profile/$', views.TambahProfile, name='tambah-profile'),
	url(r'^$', views.ProfileViews, name='profile'),
	url(r'^detail-profile/(?P<pk>[0-9]+)$', views.DetailProfile, name='detail-profile'),
	url(r'^edit-profile/(?P<pk>[0-9]+)$', views.EditProfile, name='edit-profile'),
	url(r'^delete-profile/(?P<pk>[0-9]+)$', views.DeleteProfile, name='delete-profile'),
	#JABATAN
	url(r'^tambah-jabatan/$', views.TambahJabatan, name='tambah-jabatan'),
	url(r'^jabatan/$', views.JabatanViews, name='jabatan'),
	url(r'^detail-jabatan/(?P<pk>[0-9]+)$', views.DetailJabatan, name='detail-jabatan'),
	url(r'^edit-jabatan/(?P<pk>[0-9]+)$', views.EditJabatan, name='edit-jabatan'),
	url(r'^delete-jabatan/(?P<pk>[0-9]+)$', views.DeleteJabatan, name='delete-jabatan'),
]