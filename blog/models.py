# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Consulta(models.Model):
    
    # Lista de Estados    
    LISTA_ESTADOS = (
        ('32766', 'SP-Cachoeira Paulista Antiga'),
        ('32659', 'SP-Cachoeira Paulista HIDRO'),
        ('31000', 'SP-Cachoeira Paulista Met'),
    )
    
    estado = models.CharField(max_length=5, choices=LISTA_ESTADOS)
    data_inicio = models.DateField(default=timezone.now)
    data_fim = models.DateField(default=timezone.now)

    def __str__(self):
        return self.estado