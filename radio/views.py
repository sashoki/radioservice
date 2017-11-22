# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect, get_object_or_404, HttpResponse
from radio.models import News, Service, Tariff, Tarifu, Tarifdd, Telefon, Email, Adressa, Photo, Item
from django.core.paginator import Paginator
from django.core.context_processors import csrf
from forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponseRedirect
from django.dispatch import receiver
from django.core.signals import request_finished
from django.conf import settings

# Create your views here.


def index(request):
    return render(request, 'index.html')


def newss(request, page_number=1):
    args = {}
    all_newss = News.objects.all()
    current_page = Paginator(all_newss, 4)
    args['newss'] = current_page.page(page_number)
    return render(request, 'newss.html', args)

def news(request, news_id=1):
    args = {}
    args.update(csrf(request))
    args['news'] = News.objects.get(id=news_id)
    return render(request, 'news.html', args)


def services(request):
    args = {}
    args['services'] = Service.objects.all()
    return render(request, 'services.html', args)

def service(request, service_id=1):
    args = {}
    args.update(csrf(request))
    args['service'] = Service.objects.get(id=service_id)
    return render(request, 'service.html', args)

def tariffs(request):
    args = {}
    args['tariffs'] = Tariff.objects.all()
    args['tarifus'] = Tarifu.objects.all()
    args['tarifdds'] = Tarifdd.objects.all()
    return render(request, 'tariffs.html', args)

def payment(request):
    return render(request, 'payment.html')

def connect(request):
    return render(request, 'connect.html')

def contacts(request):
    args = {}
    args['telefons'] = Telefon.objects.all()
    args['emails'] = Email.objects.all()
    args['adressas'] = Adressa.objects.all()
    return render(request, 'contacts.html', args)

def comanda(request):
    return render(request, 'comanda.html')


def fotogalerys(request):
    args = {}
    args['items'] = Item.objects.all()
    return render(request, 'fotogalerys.html', args)



def fotogalery(request, item_id=1):
    args = {}
    args.update(csrf(request))
    args['item'] = Item.objects.get(id=item_id)
    args['photos'] = Photo.objects.filter(photo_item_id=item_id)
    return render(request, 'fotogalery.html', args)

# Функція форми зворотнього звязку
def callback(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter a name.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid email address.')
        if not errors:
            send_mail(
                request.POST['name'],
                request.POST['message'],
                request.POST.get('email', 'settings.EMAIL_HOST_USER'),
                ['support@radioservice.net.ua'], # Майл на який буде відправлено лист!
            )
            return render(request, 'thanks.html')
    return render(request, 'callback.html', {
        'error': errors,
        'name': request.POST.get('name', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })





'''def callback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Якщо форма заповнена коректно, зберегти всі введені користувачем значення
        if form.is_valid():
            name = form.cleaned_data['name']
            phon = form.cleaned_data['phon']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recepients = settings.EMAIL_HOST_USER
            # Якщо користувач хоче отримати копію собі, додаємо його до списку отримувачів
            if copy:
                recepients.append(email)
            try:
                fullemail = phon + " " + email + " " + "<" + recepients + ">"
                send_mail(name, message, fullemail, ['ideauspeha@gmail.com'])
                return render(request, 'thanks.html')
            except BadHeaderError: # Захист від вразливості
                return render(request, 'callback.html')
            # Перехід на іншу сторінку, якщо повідомлення відправлено
        else:
            return render(request, 'callback.html')
    else:
        return render(request, 'callback.html')'''

'''def callback(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    # Якщо користувач хоче отримати копію собі, додаємо його до списку отримувачів
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['ideauspeha@gmail.com'])
        except BadHeaderError: # Захист від вразливості
            return HttpResponse('Invalid header found')
        # Перехід на іншу сторінку, якщо повідомлення відправлено
        return HttpResponseRedirect('/contacts/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')'''


def thanks(request):
    thanks = 'thanks'
    return render(request, 'thanks.html', {'thanks': thanks})