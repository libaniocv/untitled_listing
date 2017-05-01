#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from . import models


##USUARIOS

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserPerfil
        fields = ('foto',)