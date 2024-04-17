from typing import Any
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View


class HomeListView(View):
    template_name = "home/home.html"

    def get(self, request):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render())

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context
