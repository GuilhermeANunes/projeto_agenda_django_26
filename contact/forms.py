from django import forms
from contact.models import Contact, Category
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Just letters',
            }
        ),
        label='First Name',
        help_text='Input your firts name.'
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Just letters',
            }
        )
    )

    phone = forms.CharField(
        widget= forms.NumberInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': '(11)97979-9797',
            }
        )
    )

    email = forms.CharField(
        widget= forms.EmailInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'example@example.com',
            }
        )
    )

    description = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Descript the contact here',
            }
        )
    )  

    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    ) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture'
        )
    
    def clean(self):

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome e último nome são iguais',
                    code='invalid'
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()