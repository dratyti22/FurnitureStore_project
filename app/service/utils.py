from django.core.serializers.json import DjangoJSONEncoder
from django.core.files.uploadedfile import InMemoryUploadedFile


class CustomJsonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, InMemoryUploadedFile):
            return str(obj)
        return super().default(obj)
