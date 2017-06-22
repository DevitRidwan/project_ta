from django import forms
from .models import TransaksiMasuk, TransaksiKeluar
from django.utils import timezone

class TransaksiMasukForm(forms.ModelForm):
	kd_masuk = forms.CharField(max_length=25, label='Kode Transaksi')
	tgl_masuk= forms.DateTimeField(initial=timezone.now(), label='Tanggal Transaksi')
	class Meta:
		model = TransaksiMasuk
		fields = '__all__'

class TransaksiKeluarForm(forms.ModelForm):
    class Meta:
        model = TransaksiKeluar
        fields = '__all__'
    