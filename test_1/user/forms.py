from .models import Categories
from django.forms import ModelForm, TextInput

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["cats"]
        widgets = {"cats": TextInput(attrs={'class': 'form-control', 'placeholder': 'Input task'})
                   }