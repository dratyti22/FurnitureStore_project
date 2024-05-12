import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "furea_backend.settings")


app = Celery("furea_backend")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
