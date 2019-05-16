from django import forms

form_style = {'class': 'form-control'}


class LoginForm(forms.Form):
    studentID = forms.IntegerField(label='学号', widget=forms.TextInput(attrs=form_style))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs=form_style))







