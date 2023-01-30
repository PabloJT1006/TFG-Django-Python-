from django import forms
from django.core import validators

class FormContacto(forms.Form):
    name = forms.CharField(
        label = 'Name*',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'Placeholder':'Enter your name',
                'class': 'name'
            }
        ),

        validators=[
            validators.MinLengthValidator(1,'Introduzca su nombre'),

        ]
    )


    email=forms.EmailField(
        label='Email*',
        max_length=30,
        required=True,

        widget=forms.EmailInput(
            attrs={
                'placeholder':'Enter your email',
                'class':'email'
            }
        ),

    )

    project=forms.CharField(
        label='Project',
        max_length=30,
        required=False,

           widget=forms.TextInput(
            attrs={
                'placeholder':'Write your subject',
                'class':'project'
            }
        ),

    )

    message=forms.CharField(
        label="Message",
        max_length=100,
        required=False,

          widget=forms.Textarea(
            attrs={
                'placeholder':'Write your message',
                'class':'message'
            }
            
          ),
    )