from django import forms
from .models import Item

class ItemRequest(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'desc', 'image', 'price']