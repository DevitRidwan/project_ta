# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KategoriItem(models.Model):
	nama = models.CharField(max_length=25)

	def __unicode__(self):
		return self.nama

class Item(models.Model):
	kd_item = models.CharField(max_length=15)
	nama = models.CharField(max_length=25)
	katetori_item = models.ForeignKey(KategoriItem)
	deskripsi = models.TextField(blank=True)
	jumlah = models.PositiveIntegerField()

	def __unicode__(self):
		return self.nama

	class Meta:
		ordering = ['nama']

class Menu(models.Model):
	kd_menu = models.CharField(max_length=15, primary_key=True)
	photo = models.ImageField(upload_to='images')
	nama = models.CharField(max_length=25)
	deskripsi = models.TextField()
	item = models.ForeignKey(Item, help_text='Item utama yang digunakan')
	harga = models.PositiveIntegerField()