from django import forms

from app.home.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("first_name", "last_name",
                  "phone_number", "email", "message")
