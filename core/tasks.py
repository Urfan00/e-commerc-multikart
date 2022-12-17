from celery import shared_task
from accounts.models import User
from django.conf import settings
from .models import Subscribe
from products.models import ProductVersion
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_mail_to_subscribers():
    email_list = Subscribe.objects.values_list('email', flat=True)
    products = ProductVersion.objects.all()[:3]
    message =  render_to_string('email-subscribers.html', {
            "products" : products
        })
    subject = 'New Products From Our Website'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'html'
    mail.send()
