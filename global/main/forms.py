from django import forms
from .models import Device, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)



class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('category', 'title', 'author', 'year', 'country', 'camera', 'dynamic', 'display', 'ram', 'memory',
                  'text', 'photo', 'price', 'type_device', 'link')
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'forms-device'}),
            'title': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Назва пристрою'}),
            'year': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Рік випуску'}),
            'country': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Країна-виробник'}),
            'camera': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Кільскість камер'}),
            'dynamic': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Кільскість динаміків'}),
            'type_device': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Тип техніки'}),
            'display': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Діагональ дисплею'}),
            'ram': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Оперативна память'}),
            'link': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Оперативна память'}),
            'memory': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Внутрішня память'}),
            'price': forms.TextInput(attrs={'class': 'forms-device', 'placeholder': 'Ціна'}),
            'text': forms.Textarea(attrs={'class': 'forms-device', 'placeholder': 'Опис техніки'}),
            'author': forms.TextInput(attrs={'class': 'forms-device', 'value': '', 'id': 'elder', 'type': 'hidden'})
        }

