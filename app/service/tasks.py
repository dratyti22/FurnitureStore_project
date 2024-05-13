from celery import shared_task

from ..users.email import send_activate_user, user_mailing_list, user_maling


@shared_task
def send_activate_user_task(user_id: int):
    return send_activate_user(user_id)


@shared_task
def user_mailing_list_task(email, user_id=None):
    return user_mailing_list(email, user_id)


@shared_task
def user_maling_task(subject, message, img=None):
    return user_maling(subject, message, img)
