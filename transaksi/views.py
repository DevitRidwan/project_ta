# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import TransaksiMasukForm, TransaksiKeluarForm
from .models import TransaksiMasuk, TransaksiKeluar

#TRANSAKSI MASUK
def TransaksiMasukViews(request):
	transaksi = TransaksiMasuk.objects.all()
	return render(request, 'transaksi_masuk/view-transaksi-masuk-all.html', {'transaksi':transaksi})

def DetailTransaksiMasuk(request, pk):
	transaksi = TransaksiMasuk.objects.get(pk=pk)
	return render(request, 'transaksi_masuk/detail-transaksi-masuk.html', {'transaksi':transaksi})

def TambahTransaksiMasuk(request):
	form = TransaksiMasukForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(TransaksiMasukViews)
	return render(request, 'transaksi_masuk/tambah-transaksi-masuk.html', {'form':form})

def EditTransaksiMasuk(request, pk):
	transaksi = TransaksiMasuk.objects.get(pk=pk)
	form = TransaksiMasukForm(request.POST or None, instance=transaksi)
	if form.is_valid():
		form.save()
		return redirect(TransaksiMasukViews)
	return render(request, 'transaksi_masuk/edit-transaksi-masuk.html', {'form':form})

def DeleteTransaksiMasuk(request, pk):
	transaksi = TransaksiMasuk.objects.get(pk=pk)
	if request.method=='POST':
		transaksi.delete()
		return redirect(TransaksiMasukViews)
	return render(request, 'transaksi_masuk/delete-transaksi-masuk.html', {'object':transaksi})

#TRANSAKSI KELUAR
def TransaksiKeluarViews(request):
	transaksi = TransaksiKeluar.objects.all()
	return render(request, 'transaksi_keluar/view-transaksi-kaluar-all.html', {'transaksi':transaksi})

def DetailTransaksiKeluar(request, pk):
	transaksi = TransaksiKeluar.objects.get(pk=pk)
	return render(request, 'transaksi_keluar/detail-transaksi-keluar.html', {'transaksi':transaksi})

def TambahTransaksiKeluar(request):
	form = TransaksiKeluarForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(TransaksiKeluarViews)
	return render(request, 'transaksi_keluar/tambah-transaksi-keluar.html', {'form':form})

def EditTransaksiKeluar(request, pk):
	transaksi = TransaksiKeluar.objects.get(pk=pk)
	form = TransaksiKeluarForm(request.POST or None, instance=transaksi)
	if form.is_valid():
		form.save()
		return redirect(TransaksiKeluarViews)
	return redner(request, 'transaksi_keluar/edit-transaksi-keluar.html', {'form':form})

def DeleteTransaksiKeluar(request, pk):
	transaksi = TransaksiKeluar.objects.get(pk=pk)
	if request.method=='POST':
		transaksi.delete()
		return redirect(TransaksiKeluarViews)
	return render(request, 'transaksi_keluar/delete-transaksi-keluar.html', {'object':transaksi})