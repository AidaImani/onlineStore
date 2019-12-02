from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, label="نام")
    email = forms.EmailField(max_length=500, label="ایمیل")
    comment = forms.CharField(label='پیام', widget=forms.Textarea(
        attrs={'placeholder': 'پیام خود را وارد کنید'}))
