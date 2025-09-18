from django import forms
from catalog.models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'is_active')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                # Специальная стилизация для булевого поля
                field.widget.attrs['class'] = 'form-check-input'
            else:
                # Стилизация для всех остальных полей
                field.widget.attrs['class'] = 'form-control'


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(word in name.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError('Имя продукта содержит запрещенные слова.')
        return name


    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError('Описание продукта содержит запрещенные слова.')
        return description


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена продукта не может быть отрицательной.')
        return price
