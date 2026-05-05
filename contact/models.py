from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#id - É gerado automaticamente pelo Django
#first_name (string), last_name(string), phone(string)
#email(email), created_date(date), description(text)
#category(foreing key), show(boolean), owner(foreing key)
#picture(image)

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, )
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=500, blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'