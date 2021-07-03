from django import forms
from apps.users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    # Styling front-end register page
    email = forms.EmailField(required=True, max_length=255, widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # Deactivating labels and adding class attributes to input fields
        self.fields['email'].label = False
        self.fields['email'].widget.attrs['class'] = 'input mb-3'
        self.fields['password1'].label = False
        self.fields['password1'].widget.attrs['class'] = 'input mb-3'
        self.fields['password2'].label = False
        self.fields['password2'].widget.attrs['class'] = 'input mb-3'
