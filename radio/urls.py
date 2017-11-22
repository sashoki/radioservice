from django.conf.urls import url, include
from django.contrib import admin

from django.contrib import admin
admin.autodiscover()


urlpatterns = [


    url(r'^comanda/$', 'radio.views.comanda', name='comanda'),
    url(r'^tariffs/$', 'radio.views.tariffs', name='tariffs'),
    url(r'^payment/$', 'radio.views.payment', name='payment'),
    url(r'^connect/$', 'radio.views.connect', name='connect'),
    url(r'^contacts/$', 'radio.views.contacts', name='contacts'),
    url(r'^callback/$', 'radio.views.callback', name='callback'),
    url(r'^contacts/thanks/$', 'radio.views.callback', name='thanks'),
    url(r'^fotogalerys/get/(?P<item_id>\d+)/$', 'radio.views.fotogalery', name='fotogalery'),
    url(r'^services/get/(?P<service_id>\d+)/$', 'radio.views.service', name='service'),
    url(r'^newss/get/(?P<news_id>\d+)/$', 'radio.views.news', name='news'),
    url(r'^page/(\d+)/$', 'radio.views.newss', name='newss'),

    url(r'^fotogalerys/$', 'radio.views.fotogalerys', name='fotogalerys'),
    url(r'^services/$', 'radio.views.services', name='services'),
    url(r'^$', 'radio.views.newss', name='newss'),
    #url(r'^$', 'radio.views.callback', name='callback'),


    ]
