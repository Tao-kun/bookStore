from django import forms



form_style = {'class': 'form-control'}


class LoginForm(forms.Form):
    studentID = forms.IntegerField(label='学号', widget=forms.TextInput(attrs=form_style))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs=form_style))


class RegisterForm(forms.Form):
    studentID = forms.IntegerField(label='学号', widget=forms.TextInput(attrs=form_style))
    name = forms.CharField(label='姓名', max_length=256, widget=forms.TextInput(attrs=form_style))
    password1 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs=form_style))
    password2 = forms.CharField(label='确认密码', max_length=256, widget=forms.PasswordInput(attrs=form_style))
    email = forms.EmailField(label='Email', max_length=256, widget=forms.EmailInput(attrs=form_style))
