from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail


def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        comment = form.cleaned_data.get("comment")

        subject = name + ':' + comment
        comment = email + ':' + comment
        send_mail(subject, comment, 'aidaimani76@gmail.com', ['imanifatemeh235@gmail.com'])

        return redirect('/')

    else:
        context = {'form': form}
        return render(request, 'contact/contact.html', context)

