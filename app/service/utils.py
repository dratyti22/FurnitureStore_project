from django.core.serializers.json import DjangoJSONEncoder
from django.core.files.uploadedfile import InMemoryUploadedFile

from summa import summarizer


class CustomJsonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, InMemoryUploadedFile):
            return str(obj)
        return super().default(obj)


def title_in_message(message):
    """
    Выделяет основную мысль из message
    """
    summary = summarizer.summarize(message, ratio=0.3, language="russian")
    return f'{summary[:200]}'
