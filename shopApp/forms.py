from django.forms import ModelForm
from .models import shopingItem

class shopingItem(ModelForm):
    class Meta:
        model=shopingItem
        fields='__all__'