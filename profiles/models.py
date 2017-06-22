# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here.
JENIS_GAJI = (
	('bulan', 'bulan'),
	('hari', 'hari'),
	('jam', 'jam')
	)

class Jabatan(models.Model):
	nama_jabatan = models.CharField(max_length=15)
	nominal = models.IntegerField(null=True)
	jenis_gaji = models.CharField(max_length=5, choices=JENIS_GAJI)

	def __unicode__(self):
		return self.nama_jabatan

class Profiles(models.Model):
	kd_profile = models.CharField(max_length=10, primary_key=True)
	nama = models.CharField(max_length=30)
	status_user = models.BooleanField(default=False)
	username = models.CharField(max_length=15, blank=True)
	jabatan = models.ForeignKey(Jabatan)
	tgl_lahir = models.DateField(default=date.today())
	alamat_skr = models.CharField(max_length=75)
	email = models.EmailField(blank=True)

	def __unicode__(self):
		return self.nama