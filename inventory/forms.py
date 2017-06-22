from django import forms
from .models import Item, KategoriItem, Menu

class ItemForm(forms.ModelForm):
	if Item.objects.count()<=0:
		kd_item = forms.CharField(max_length=10, initial='1000000001')
	else:
		kode = int(Item.objects.latest('pk').kd_item) + 1
		kd_item = forms.CharField(max_length=10, initial=kode, label='Kode Profile')
	harga = forms.IntegerField(label='Harga Jual')
	class Meta:
		model = Item
		fields = '__all__'

class KategoriItemForm(forms.ModelForm):
	class Meta:
		model = KategoriItem
		fields = '__all__'

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'