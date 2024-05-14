from celery import shared_task

from .email import send_activate_user, user_mailing_list, user_maling, send_contact_email_message


@shared_task
def send_activate_user_task(user_id: int):
    return send_activate_user(user_id)


@shared_task
def user_mailing_list_task(email, user_id=None):
    return user_mailing_list(email, user_id)


@shared_task
def user_maling_task(subject, message, img=None):
    return user_maling(subject, message, img)


@shared_task
def send_contact_email_message_task(first_name, last_name, phone_number, email, message, user_id):
    return send_contact_email_message(first_name, last_name, phone_number, email, message, user_id)
