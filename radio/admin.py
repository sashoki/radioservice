# -*- coding: utf-8 -*-


from django.contrib import admin
from radio.models import News, Service, Tariff, Tarifu, Tarifdd, Telefon, Email, Adressa, Item, Photo



class NewsAdmin(admin.ModelAdmin):
    fields = ['news_date', 'news_image', 'news_title', 'news_text', 'video']
    list_display = ('news_date', 'news_image', 'news_title', 'video')
    search_fields = ['news_date']

class ServiceAdmin(admin.ModelAdmin):
    fields = ['service_title', 'service_image', 'service_text', 'video']
    list_display = ('service_title', 'service_image', 'video')
    search_fields = ['service_title']

class TariffAdmin(admin.ModelAdmin):
    fields = ['tariff_speed', 'tariff_lviv', 'tariff_oblast', 'tariff_district', 'tariff_date']
    list_display = ('tariff_speed', 'tariff_lviv', 'tariff_oblast', 'tariff_district', 'tariff_date')
    search_fields = ['tariff_speed']

class TarifuAdmin(admin.ModelAdmin):
    fields = ['tarifu_speed', 'tarifu_lviv', 'tarifu_oblast', 'tarifu_dinip', 'tarifu_statip', 'tarifu_date']
    list_display = ('tarifu_speed', 'tarifu_lviv', 'tarifu_oblast', 'tarifu_dinip', 'tarifu_statip', 'tarifu_date')
    search_fields = ['tarifu_speed']

class TarifddAdmin(admin.ModelAdmin):
    fields = ['tarifdd_title', 'tarifdd_pay', 'tarifdd_date']
    list_display = ('tarifdd_title', 'tarifdd_pay', 'tarifdd_date')
    search_fields = ['tarifdd_title']

class TelefonAdmin(admin.ModelAdmin):
    fields = ['telefon_nn', 'telefon_telefon', 'telefon_viddil', 'telefon_date']
    list_display = ('telefon_nn', 'telefon_telefon', 'telefon_viddil', 'telefon_date')
    search_fields = ['telefon_viddil']

class EmailAdmin(admin.ModelAdmin):
    fields = ['email_nn', 'email_viddil', 'email_email', 'email_date']
    list_display = ('email_nn', 'email_viddil', 'email_email', 'email_date')
    search_fields = ['email_viddil']

class AdressaAdmin(admin.ModelAdmin):
    fields = ['adressa_adressa']

class ItemInline(admin.StackedInline):
    model = Photo
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


admin.site.register(News, NewsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Tariff, TariffAdmin)
admin.site.register(Tarifu, TarifuAdmin)
admin.site.register(Tarifdd, TarifddAdmin)
admin.site.register(Telefon, TelefonAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Adressa, AdressaAdmin)
admin.site.register(Item, ItemAdmin)




