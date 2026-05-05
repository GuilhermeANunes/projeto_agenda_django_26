from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    contact_list = Contact.objects.all().filter(show=True).order_by('-id')
    paginator = Paginator(contact_list, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Home - ',
    }

    return render (
        request,
        'contact/index.html',
        context,
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.get(id=contact_id)
    single_contact = get_object_or_404(Contact, id = contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render (
        request,
        'contact/contact.html',
        context,
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('index')

    search_contact = Contact.objects\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .filter(show=True)\
        .order_by('-id')
    
    paginator = Paginator(search_contact, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render (
        request,
        'contact/index.html',
        context,
    )