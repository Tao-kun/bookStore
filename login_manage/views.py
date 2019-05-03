from django.shortcuts import render, redirect

from login_manage.forms import RegisterForm, LoginForm
from login_manage.models import User


def index(request):
    return render(request, "login_manage/index.html")


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST, request.FILES)
        message = ""
        if login_form.is_valid():
            studentID = login_form.cleaned_data['studentID']
            password = login_form.cleaned_data['password']
            try:
                student = User.objects.get(studentID=studentID)
                print(password)
                print(student.password)
                if password == student.password:
                    request.session['studentID'] = student.studentID
                    request.session['name'] = student.name
                    request.session['is_login'] = True
                    return redirect('/index/')
                else:
                    message = "密码错误！"
            except:
                message = "学号错误！"
    login_form = LoginForm(request.POST)
    return render(request, "login_manage/login.html", locals())



def register(request):
    request.session.flush()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        message = "请再次检查要填写的内容"
        if register_form.is_valid():
            studentID = register_form.cleaned_data['studentID']
            name = register_form.cleaned_data['name']
            pwd1 = register_form.cleaned_data['password1']
            pwd2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']

            # 如果这个ID已经注册过账号，那么不允许再注册
            IsSame = User.objects.filter(studentID=studentID)
            if IsSame:
                jump_to_login = True
                request.session.flush()
                return render(request, 'login_manage/login.html', locals())
            # 两次的密码输入要一致

            if pwd1 != pwd2:
                diffpwd = True
                return render(request, 'login_manage/login.html', locals())
            else:
                diffpwd = False

            # 正常情况，创建用户加入数据库
            new_usr = User()
            new_usr.studentID = int(studentID)
            new_usr.name = name
            new_usr.password = pwd1
            new_usr.email = email
            new_usr.save()
    register_form = RegisterForm()
    return render(request, "login_manage/register.html", locals())


def test(request):
    return render(request, "login_manage/test.html")
