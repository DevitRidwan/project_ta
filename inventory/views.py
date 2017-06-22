# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Item, KategoriItem, Menu
from .forms import ItemForm, KategoriItemForm, MenuForm
#ITEMS

def ItemViews(request):
	items = Item.objects.all()
	return render(request, 'item/item-view-all.html', {'items':items})

def DetailItem(request, pk):
	item = Item.objects.get(pk=pk)
	return render(request, 'item/detail-item.html', {'item':item})

def TambahItem(request):
	form = ItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(ItemViews)
	return render(request, 'item/tambah-item.html', {'form':form})

def EditItem(request, pk):
	item = Item.objects.get(pk=pk)
	form = ItemForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		return redirect(request, 'item/edit-item.html', {'form':form})

def DeleteItem(request, pk):
	item = Item.objects.get(pk=pk)
	if request.method=='POST':
		item.delete()
		return redirect(ItemViews)
	return render(request, 'item/delete-item.html', {'object':item})

#KATEGORI ITEM

def KategoriItemView(request):
	kategori = KategoriItem.objects.all()
	return render(request, 'kategori_item/view-kategori-item.html', {'kategori':kategori})

def DetailKategoriItem(request, pk):
	kategori = KategoriItem.objects.get(pk=pk)
	return render(request, 'kategori_item/detail-kategori-item.html', {'kategori':kategori})

def TambahKategoriItem(request):
	form = KategoriItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(KategoriItemView)
	return render(request, 'kategori_item/tambah-kategori-item.html', {'form':form})

def EditKategoriItem(request, pk):
	kategori = KategoriItem.objects.get(pk=pk)
	form = KategoriItemForm(request.POST or None, instance=kategori)
	if form.is_valid():
		form.save()
		return redirect(KategoriItemView)
	return render(request, 'kategori_item/edit-kategori-item.html', {'form':form})

def DeleteKategoriItem(request, pk):
	kategori = KategoriItem.objects.get(pk=pk)
	if request.method=='POST':
		kategori.delete()
		return redirect(KategoriItemView)
	return render(request, 'kategori_item/delete-kategori-item.html', {'object':kategori})

#MENU
def MenuViews(request):
	menu = Menu.objects.all()
	return render(request, 'menu/menu-view.html', {'menu':menu})

def TambahMenu(request):
	form  = MenuForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(MenuViews)
	return render(request, 'menu/tambah-menu.html', {'form':form})

def EditMenu(request, pk):
	menu = Menu.objects.get(pk=pk)
	form = MenuForm(request.POST or None, instance=menu)
	if form.is_valid():
		form.save()
		return redirect(MenuViews)
	return render(request, 'menu/edit-menu.html', {'form':form})

def DeleteMenu(request, pk):
	menu = Menu.objects.get(pk=pk)
	if request.method=='POST':
		menu.delete()
		return redirect(MenuViews)
	return render(request, 'menu/delete-menu.html', {'object':menu})