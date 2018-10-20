from .models import Future, Choice
from django import forms


class FutureForm(forms.ModelForm):
    class Meta:
        model = Future
        fields = ('title', 'date', 'usage')


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('title', 'place', 'link', 'price', 'image')
