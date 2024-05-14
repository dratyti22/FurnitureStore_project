from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from app.home.models import Feedback

from .forms import FeedbackForm
from ..service.tasks import send_contact_email_message_task


class HomeListView(View):

    def get(self, request):
        return render(request, "home/home.html")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context


class Contact(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "home/contact.html"
    success_url = reverse_lazy("home:home")

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Feedback"
        return context

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            if self.request.user.is_authenticated:
                feedback.user = self.request.user
                send_contact_email_message_task.delay(feedback.first_name, feedback.last_name, feedback.phone_number,
                                                      feedback.email, feedback.message, self.request.user.id)
        return super().form_valid(form)
