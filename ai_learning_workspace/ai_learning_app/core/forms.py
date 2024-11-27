from django import forms
from .models import Avatar

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['hair_color', 'skin_tone', 'accessories']


ACCESSORY_CHOICES = [
    ('glasses', 'Glasses'),
    ('hat', 'Hat'),
    ('earrings', 'Earrings'),
    ('necklace', 'Necklace'),
    ('bracelet', 'Bracelet'),
]

class AvatarForm(forms.ModelForm):
    accessories = forms.MultipleChoiceField(
        choices=ACCESSORY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Accessories"
    )

    class Meta:
        model = Avatar
        fields = ['hair_color', 'skin_tone', 'accessories']
