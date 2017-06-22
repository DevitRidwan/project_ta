# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from inventory.models import Item
from profiles.models import Profiles
from datetime import datetime

# Create your models here.
class TransaksiMasuk(models.Model):
	kd_masuk = models.CharField(max_length=25, primary_key=True)
	tgl_masuk = models.DateTimeField(default=datetime.now())
	user = models.ForeignKey(Profiles)
	item = models.ForeignKey(Item)
	jumlah = models.PositiveIntegerField()
	bayar = models.PositiveIntegerField()

	class QuickReport():
		date_field = "tgl_masuk"

class TransaksiKeluar(models.Model):
	kd_keluar = models.CharField(max_length=25, primary_key=True)
	tgl_keluar = models.DateTimeField(default=datetime.now())
	user = models.ForeignKey(Profiles)
	item = models.ForeignKey(Item)
	harga = models.PositiveIntegerField()
	jumlah = models.PositiveIntegerField()

class DummyTransaksi(models.Model):
	kd = models.CharField(max_length=25, primary_key=True)
	tgl_masuk = models.DateTimeField(default=datetime.now())
	user = models.ForeignKey(Profiles)
	item = models.ForeignKey(Item)
	jumlah = models.PositiveIntegerField()
	bayar = models.PositiveIntegerField()