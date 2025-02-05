from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ImageField, FileInput, DateInput, FileField


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Confirm Password"})) 
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']



class DateInput(forms.DateInput):
    input_type = 'date'


class UserInfoForm(forms.ModelForm):
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(
        #choices=[('M', 'Male'), ('F', 'Female')],
        choices=GENDER,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"})
    ) 
    marital = forms.ChoiceField(
        choices=MARITAL_STATUS,
        required=True,
        #choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced')],
        widget=forms.Select(attrs={"class":"form-control"})
        )
    phone_number = forms.IntegerField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    lga = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    residential_address = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    identity_type = forms.ChoiceField(
        choices=IDENTITY_TYPE,
        required=True,
        widget=forms.Select(attrs={"class":"form-control"}))
    identity_image = FileField(required=True, widget=FileInput (attrs={"class":"form-control", 'accept': 'image/jpeg,image/png'}))
    passport = FileField(required=True, widget=FileInput (attrs={"class":"form-control", 'accept': 'image/jpeg,image/png'}))
    date_of_birth = forms.DateInput
    signature = FileField(required=True, widget=FileInput (attrs={"class":"form-control", 'accept': 'image/jpeg,image/png'}))
    next_of_kin = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    kin_number = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    


    class Meta:
        model = UserInfo
        fields = [
            'full_name',
            'gender',
            'marital',
            'phone_number',
            'state',
            'lga',
            'residential_address',
            'identity_type',
            'identity_image',
            'passport',
            'date_of_birth',
            'signature',
            'next_of_kin',
            'kin_number',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={"class":"form-control",'type': 'date'}),
        }
        