from typing import Any
from django.shortcuts import render
from django.views.generic import View


class HomeListView(View):

    def get(self, request):
        return render(request, "home/home.html")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context
