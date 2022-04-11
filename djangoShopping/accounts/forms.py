from django.contrib.auth import get_user_model
from . models import ESUser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ESUserCreationForm(UserCreationForm):

    # dodanie ekstra pól do modelu uzytkownika
    class Meta:
        model = ESUser
        # fields = UserCreationForm.fields + ('origin', 'sex')
        fields = ['username',  'sex', 'password1', 'password2', 'email', 'origin', 'profile_pic']

        widgets = {
            'sex': forms.Select(attrs={'class': 'bootstrap-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['username'].label = 'Enter your name'
        self.fields['email'].label = 'Enter your email address'
        self.fields['origin'].label = 'Input your country of origin'
