# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.

class Process(models.Model):
    id = models.AutoField(primary_key=True)
    method_type = models.CharField(max_length=255, db_index=True)
    header = models.TextField(default='')
    time = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=256, blank=True, null=True)
    query = models.CharField(max_length=256, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'process'

