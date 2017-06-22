from .models import Profiles, Jabatan
from django import forms
from datetime import date
from django.forms.extras.widgets import SelectDateWidget

class ProfileForm(forms.ModelForm):
	if Profiles.objects.count()<=0:
		kd_profile = forms.CharField(max_length=10, initial='1000000001')
	else:
		kode = int(Profiles.objects.latest('pk').kd_profile) + 1
		kd_profile = forms.CharField(max_length=10, initial=kode, label='Kode Profile')
	nama = forms.CharField(max_length=30, label='Nama')
	status_user = forms.BooleanField(label='Status User')
	alamat_skr = forms.CharField(max_length=75, label='Alamat Sekarang')
	tgl_lahir = forms.DateField(widget=SelectDateWidget(years=range(date.today().year-30,date.today().year-18)), label='Tanggal Lahir')
	class Meta:
		model = Profiles
		fields = '__all__'

class JabatanForm(forms.ModelForm):
	class Meta:
		model = Jabatan
		fields = '__all__'