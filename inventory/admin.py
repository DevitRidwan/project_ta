# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Item, KategoriItem, Menu

# Register your models here.
admin.site.register(Item)
admin.site.register(KategoriItem)
admin.site.register(Menu)