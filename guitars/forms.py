from django import forms
from .models import Guitars


class SubmitGuitarForm(forms.ModelForm):

    class Meta:
        model = Guitars
        fields = (
            'guitar_model',
            'slug',
            'description',
            'guitar_image',
            'remaining_guitars',
            'price',
        )
        labels = {
            'guitar_model': 'Guitar Model',
            'slug': 'Repeat the Guitar Model without spaces.',
            'description': 'Description',
            'guitar_image': 'Select image',
            'remaining_guitars': 'How many guitars left?',
            'price': 'Price in Euros',
        }