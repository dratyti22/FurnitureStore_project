from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404

from .models import UserModel, EmailMailingList
from django.conf import settings


def send_activate_user(user_id):
    """
    Функция по потверждению аккаунта
    """
    user = get_object_or_404(UserModel, id=user_id)
    current_site = Site.objects.get_current().domain
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_url = reverse_lazy("users:confirm_email", kwargs={
                                  'uidb64': uid, 'token': token})
    subject = f'Активируйте свой аккаунт, {user.username}!'
    message = render_to_string('users/email/activate_email_send.html', {
        'user': user,
        'activation_url': f'http://{current_site}{activation_url}',
    })
    return user.email_user(subject, message)


def user_mailing_list(email, user_id=None):
    """
    Функция для увидомление о подключенной рассылоки
    """

    current_site = Site.objects.get_current().domain
    subject = f'Вы подписались на рассылку сообщений!'
    if user_id:
        user = get_object_or_404(UserModel, id=user_id)
        message = render_to_string('users/email/user_mailing_list.html', {
            'user': user,
            'current_site': current_site,
        })
    else:
        message = render_to_string('users/email/user_mailing_list.html', {
            'current_site': current_site,
        })

    admin = ''.join(settings.EMAIL_ADMIN)

    send_mail(subject, message, admin, [email])


def user_maling(subject, message, img=None):
    model = EmailMailingList.objects.all()
    current_site = Site.objects.get_current().domain
    if img:
        message = render_to_string('users/email/user_mailing.html',
                                   {'message': message, 'img': img, 'current_site': current_site, })
        print(img)
    else:
        message = render_to_string('users/email/user_mailing.html', {
            'message': message,
            'current_site': current_site,
        })

    for i in model:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [i.email])
