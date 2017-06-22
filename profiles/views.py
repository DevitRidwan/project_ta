# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Profiles, Jabatan
from .forms import ProfileForm, JabatanForm
from .main_profile import AddUser

#PROFILES

def ProfileViews(request):
	profiles = Profiles.objects.all()
	return render(request, 'profile/profile-view-all.html', {'profiles':profiles})

def DetailProfile(request, pk):
	profile = Profiles.objects.get(pk=pk)
	return render(request, 'profile/detail-profile.html', {'profile':profile})

def TambahProfile(request):
	form = ProfileForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(ProfileViews)
	return render(request, 'profile/tambah-profile.html', {'form':form})

def TambahUser(request, pk):
	profile = Profiles.objects.get(pk=pk)
	return AddUser(profile)

def EditProfile(request, pk):
	profile = Profiles.objects.get(pk=pk)
	form = ProfileForm(request.POST or None, instance=profile)
	if form.is_valid():
		form.save()
		return redirect(ProfileViews)
	return render(request, 'profile/edit-profile.html', {'form':form})

def DeleteProfile(request, pk):
	profiles = Profiles.objects.get(pk=pk)
	if request.method=='POST':
		profiles.delete()
		return redirect(ProfileViews)
	return render(request, 'profile/delete.profile-html', {'object':profiles})

#JABATAN

def JabatanViews(request):
	jabatan = Jabatan.objects.all()
	return render(request, 'jabatan/jabatan-view-all.html', {'jabatan':jabatan})

def DetailJabatan(request, pk):
	jabatan = Jabatan.objects.get(pk=pk)
	return render(request, 'jabatan/detail-jabatan.html', {'jabatan':jabatan})

def TambahJabatan(request):
	form = JabatanForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(JabatanViews)
	return render(request, 'jabatan/tambah-jabatan.html', {'form':form})

def EditJabatan(request, pk):
	jabatan = Jabatan.objects.get(pk=pk)
	form = JabatanForm(request.POST or None, instance=jabatan)
	if form.is_valid():
		form.save()
		return redirect(JabatanViews)
	return render(request, 'jabatan/edit-jabatan.html', {'form':form})

def DeleteJabatan(request, pk):
	jabatan = Jabatan.objects.get(pk=pk)
	if request.method=='POST':
		jabatan.delete()
		return redirect(JabatanViews)
	return render(request, 'jabatan/delete-jabatan.html', {'object':jabatan})