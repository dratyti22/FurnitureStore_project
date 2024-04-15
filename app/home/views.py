from typing import Any
from django.shortcuts import render
from django.views.generic import ListView

# class HomeListView(ListView):
#     template_name = "main.html"

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Home"
#         return context
def HomeListView(request):
    context = {
        "title": "Home"
    }
    return render(request, "home/home.html", context)
