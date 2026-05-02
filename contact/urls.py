from django.urls import path
from contact.views import index_view

urlpatterns = [
    path('', index_view.index, name='index'),
]
