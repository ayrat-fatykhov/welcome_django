from django import forms
from django.forms import ModelForm

from catalog.models import Product, Version


class StyleFormMixin:
    """
    Миксин для стилизации форм
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """
    Переопределяет заполняемые поля для форм продукта
    """

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price',)

    def clean_name(self):
        """
        Вводит ограничение в виде недопустимых слов в названии продукта
        """
        cleaned_data = self.cleaned_data['name']

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('''Наименование продукта не должно содержать следующие слова: 
                казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.''')

        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    """
    Определяет выводимые поля в форме для группы 'Модератор'
    """
    class Meta:
        model = Product
        fields = (
            "is_publish",
            "description",
            "category",
        )
