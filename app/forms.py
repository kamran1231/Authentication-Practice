from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'})
        }

# class ChangePasswordForm(PasswordChangeForm):
#     class Meta:
#
#         widgets = {
#             'old_password':forms.PasswordInput(attrs={'class':'form-control'}),
#             'new_password1':forms.PasswordInput(attrs={'class':'form-control'}),
#             'new_password2':forms.PasswordInput(attrs={'class':'form-control'}),
#
#     }
