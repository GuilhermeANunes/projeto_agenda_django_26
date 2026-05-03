from django.shortcuts import render
from contact.forms import ContactForm

# Create your views here.
def create(request):

    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST),
            'site_title': 'Create - ',
        }

        return render (
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': ContactForm,
        'site_title': 'Create - ',
    }

    return render (
        request,
        'contact/create.html',
        context,
    )