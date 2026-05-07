from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from contact.models import Contact, Category
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

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
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Este e-mail já está cadastrado.', code='invalid')
            )
        
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
        help_text='Required',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )

    last_name = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
        help_text='Required.'
    )

    email = forms.EmailField(
        min_length=3,
        max_length=50,
        required=True,
    )

    username = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text= password_validation.password_validators_help_text_html(),
        required=True,
    )

    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text= 'Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        
        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('passord1')
        password2 = self.cleaned_data.get('passord2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não conferem.')
                )


    def clean_email(self):
        email = self.cleaned_data.get('email')

        current_email = self.instance.email

        if current_email != email:

            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Este e-mail já está cadastrado.', code='invalid')
                )
        
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))


        return password1
