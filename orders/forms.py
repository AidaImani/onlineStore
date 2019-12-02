from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {'first_name': 'نام',
                  'last_name': 'نام خانوادگی',
                  'email': 'ایمیل',
                  'address': 'آدرس',
                  'postal_code': 'کدپستی',
                  'city': 'شهر'}
        widgets = {
            'first_name': forms.TextInput(attrs={'style': 'background-color: #f1eeed96;'
                                                          'border-radius: 5px;box-shadow:3px','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'style': 'background-color: #f1eeed96;border-radius: 5px;'
                                                         'box-shadow:3px','class':'form-control'}),
            'email': forms.TextInput(attrs={'style': 'background-color: #f1eeed96;'
                                                     'border-radius: 5px;box-shadow:3px;','class':'form-control'}),
            'address': forms.TextInput(attrs={'style': 'background-color: #f1eeed96;'
                                                       'border-radius: 5px;box-shadow:3px;height:60px','class':'form-control'}),
            'postal_code': forms.TextInput(attrs={'style': 'background-color: #f1eeed96;'
                                                           'border-radius: 5px;box-shadow:3px;','class':'form-control'}),
            'city': forms.TextInput(attrs={'style': 'background-color: #f1eeed96;'
                                                    'border-radius: 5px;box-shadow:3px;','class':'form-control'})

        }
