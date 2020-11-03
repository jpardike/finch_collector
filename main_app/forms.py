from django import forms
from .models import Feeding, Finch

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']


class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = ('name', 'breed', 'description', 'age')