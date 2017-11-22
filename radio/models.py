# -*- coding: utf-8 -*-

from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.db import models
#from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
#import mptt
#from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class News(models.Model):
    class Meta():
        ordering = ['-news_date']
        db_table = 'News'
        verbose_name_plural = 'Новини фірми'
        verbose_name = 'Новини фірми'
    news_title = models.CharField(null=False, blank=True, max_length=200, verbose_name='Заголовок новини')
    news_text = RichTextField(null=False, blank=True, verbose_name='Основна частина')
    news_date = models.DateField(null=False, blank=True, verbose_name='Дата публікації')
    news_image = models.ImageField(null=True, blank=True, upload_to='news/', verbose_name=u'Зображення')
    video = EmbedVideoField(null=True, blank=True, verbose_name=u'Відео')

    def __unicode__(self):
        return self.news_title

    def bit_news(self):
        if self.news_image:
            return u'<img src="%s" width="70"/>' % self.news_image.url
        else:
            return u'(none)'
    bit_news.short_descriptio = u'Зображення'
    bit_news.allow_tags = True


class Service(models.Model):
    class Meta():
        db_table = 'Service'
        verbose_name_plural = 'Сервіси'
        verbose_name = 'Сервіс'
    service_title = models.CharField(null=False, blank=True, max_length=200, verbose_name='Заголовок')
    service_image = models.ImageField(null=False, blank=True, upload_to='service/', verbose_name=u'Зображення')
    service_text = RichTextField(null=False, blank=True, verbose_name='Основна частина')
    service_date = models.DateField(null=True, blank=True, verbose_name='Дата публікації')
    video = EmbedVideoField(null=True, blank=True, verbose_name=u'Відео')

    def __unicode__(self):
        return self.service_title

    def __str__(self):
        return self.service_title

class Tariff(models.Model):
    class Meta():
        ordering = ['-tariff_date']
        db_table = 'Tariff'
        verbose_name_plural = 'Тарифи для фізичних осіб'
        verbose_name = 'Тарифи для фізичних осіб'
    tariff_speed = models.CharField(null=False, blank=True, max_length=100, verbose_name='Встановлена швидкість')
    tariff_lviv = models.CharField(null=False, blank=True, max_length=100, verbose_name='м. Львів + 30км')
    tariff_oblast = models.CharField(null=False, blank=True, max_length=100, verbose_name='Область (Бродівський р-н., Сколівський р-н смт. Славське та довкола')
    tariff_district = models.CharField(null=False, blank=True, max_length=100, verbose_name='Інші райони')
    tariff_date = models.DateField(null=True, blank=True, verbose_name='Дата публікації')

    def __unicode__(self):
        return self.tariff_speed

    def __str__(self):
        return self.tariff_speed

class Tarifu(models.Model):
    class Meta():
        ordering = ['-tarifu_date']
        db_table = 'Tarifu'
        verbose_name_plural = 'Тарифи для юридичних осіб'
        verbose_name = 'Тарифи для юридичних осіб'
    tarifu_speed = models.CharField(null=False, blank=True, max_length=100, verbose_name='Встановлена швидкість')
    tarifu_lviv = models.CharField(null=False, blank=True, max_length=100, verbose_name='м. Львів + 30км')
    tarifu_oblast = models.CharField(null=False, blank=True, max_length=100, verbose_name='Область')
    tarifu_dinip = models.CharField(null=False, blank=True, max_length=100, verbose_name='Динамічна ІР-адреса')
    tarifu_statip = models.CharField(null=False, blank=True, max_length=100, verbose_name='Статична ІР-адреса')
    tarifu_date = models.DateField(null=True, blank=True, verbose_name='Дата публікації')

    def __unicode__(self):
        return self.tarifu_speed

    def __str__(self):
        return self.tarifu_speed


class Tarifdd(models.Model):
    class Meta():
        db_table = 'Taridd'
        verbose_name_plural = 'Додаткові оплати'
        verbose_name = 'Додаткові оплати'
    tarifdd_title = models.CharField(null=False, blank=True, max_length=100, verbose_name='Назва оплати')
    tarifdd_pay = models.CharField(null=False, blank=True, max_length=100, verbose_name='ціна')
    tarifdd_date = models.DateField(null=True, blank=True, verbose_name='Дата публікації')


    def __unicode__(self):
        return self.tarifdd_title

    def __str__(self):
        return self.tarifdd_title

class Telefon(models.Model):
    class Meta():
        db_table = 'Telefon'
        verbose_name_plural = 'Контактні телефони'
        verbose_name = 'Контактні телефони'
    telefon_nn = models.CharField(null=False, blank=True, max_length=100, verbose_name='Номер по порядку')
    telefon_telefon = models.CharField(null=False, blank=True, max_length=100, verbose_name='Телефон')
    telefon_viddil = models.CharField(null=False, blank=True, max_length=100, verbose_name='Відділ')
    telefon_date = models.DateField(null=True, blank=True, verbose_name='Дата публікації')


    def __unicode__(self):
        return self.telefon_nn

    def __str__(self):
        return self.telefon_nn

class Email(models.Model):
    class Meta():
        db_table = 'Email'
        verbose_name_plural = 'Електронна пошта'
        verbose_name = 'Електронна пошта'
    email_nn = models.CharField(null=False, blank=True, max_length=100, verbose_name='Номер по порядку')
    email_viddil = models.CharField(null=False, blank=True, max_length=100, verbose_name='Відділ')
    email_email = models.CharField(null=False, blank=True, max_length=100, verbose_name='Електронна адреса')
    email_date = models.DateField(null=True, blank=True, verbose_name='Дата публікації')


    def __unicode__(self):
        return self.email_nn

    def __str__(self):
        return self.email_nn

class Adressa(models.Model):
    class Meta():
        db_table = 'Adressa'
        verbose_name_plural = 'Адресса фірми'
        verbose_name = 'Адресса фірми'
    adressa_adressa = models.CharField(null=False, blank=True, max_length=200, verbose_name='Адресса фірми')


    def __unicode__(self):
        return self.adressa_adressa

    def __str__(self):
        return self.adressa_adressa

class Item(models.Model):
    class Meta():
        ordering = ['name']
        verbose_name_plural = 'Фотогалереї'
        verbose_name = 'Фотогалерея'
    name = models.CharField(max_length=100, verbose_name='Назва фотогалереї')
    image = models.ImageField(null=True, blank=True, upload_to='fotogalery/', verbose_name=u'Зображення')
    description = models.TextField(verbose_name='Опис фотогалереї')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

#@permalink
#def get_absolute_url(self):
#    return ('item_detail', None, {'object_id': self.id})

class Photo(models.Model):
    class Meta():
        ordering = ['photo_title']
        verbose_name_plural = 'фото'
        verbose_name = 'фото'

    photo_item = models.ForeignKey(Item)
    photo_title = models.CharField(blank=True, max_length=100, verbose_name=u'Назва фотографії')
    photo_image = models.ImageField(blank=True, upload_to='foto/', verbose_name=u'Зображення')
    photo_caption = models.CharField(max_length=250, blank=True, verbose_name=u'Підпис')

    def __unicode__(self):
        return self.photo_title

    def __str__(self):
        return self.photo_title

#@permalink
#def get_absolute_url(self):
#    return ('photo_detail', None, {'object_id': self.id})
