from .models import Future
from django import forms


class FutureForm(forms.ModelForm):
    class Meta:
        model = Future
        fields = '__all__'

