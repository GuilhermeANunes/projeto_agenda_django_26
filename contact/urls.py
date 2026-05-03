from django.urls import path
from contact.views import index_view

urlpatterns = [
    path('<int:contact_id>/', index_view.contact, name='single_contact'),
    path('search/', index_view.search, name='search'),
    path('', index_view.index, name='index'),
]
