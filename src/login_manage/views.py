from random import choice
import string
import re
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from login_manage import models
from login_manage.forms import LoginForm
from login_manage.models import User


# 主页，返回登录信息到主页以判断是登录注册还是注销
def index(request):
    is_login = request.session.get('is_login', None)
    if is_login:
        user = User.objects.get(pk=request.session.get('studentID'))
    return render(request, "login_manage/index.html", locals())


# 登录系统，验证账号密码，返回相应错误信息
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST, request.FILES)
        message = ""
        if login_form.is_valid():
            studentID = login_form.cleaned_data['studentID']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(studentID=studentID)
                # print(password)
                # print(user.password)
                if password == user.password:
                    request.session['studentID'] = user.studentID
                    request.session['name'] = user.name
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
    return render(request, 'login_manage/register.html', locals())


#  注销，清除session
def logout(request):
    request.session.flush()
    return render(request, 'login_manage/logout.html')


#  检验表单输入信息合法性，返回一个json
def is_valid(request):
    studentid = request.GET.get('studentid')
    password1 = request.GET.get('password1')
    password2 = request.GET.get('password2')
    email = request.GET.get('email')
    name = request.GET.get('name')
    exists_stu = models.User.objects.filter(studentID=studentid)
    exists_email = models.User.objects.filter(email=email)
    exists_name = models.User.objects.filter(name=name)
    if name:
        null_name = "false"     # 名字为空
    else:
        null_name = "true"
    if exists_name:
        same_name = "true"      # 已被注册
    else:
        same_name = "false"
    if exists_email:
        same_email = "true"     # email已有
    else:
        same_email = "false"
    if exists_stu:
        same_stu = "true"
    else:
        same_stu = "false"      # id已有
    if password1 == password2:
        same_pwd = "true"
    else:
        same_pwd = "false"      # 两次输入密码是否一致
    str = r'^([\w]+\.*)([\w]+)\@[\w]+\.\w{3}(\.\w{2}|)$'   # email正则
    if re.match(str, email) and not str.isspace():
         ok_email = "true"
         # print(email)
    else:
        ok_email = "false"
    if len(studentid) == 8 and studentid:
        ok_stuid = "true"
    else:
        ok_stuid = "false"
    ok_return = "false"
    if ok_email == "true" and ok_stuid == "true" and null_name == "false" and same_name == "false" and same_email == "false" and same_stu == "false" and same_pwd == "true":
        ok_return = "true"
    ret = {'same_pwd': same_pwd, 'ok_email': ok_email, 'ok_stuid': ok_stuid, 'ok_return': ok_return, 'same_stu': same_stu, 'same_email': same_email, 'same_name': same_name, 'null_name': null_name}
    return HttpResponse(json.dumps(ret), content_type='application/json')


def test(request):
    return render(request, "login_manage/test.html")


#  添加学生至数据库
def add_to_db(request):
    studentid = request.GET.get('studentid')
    password = request.GET.get('password')
    email = request.GET.get('email')
    name = request.GET.get('name')
    new_usr = User()
    new_usr.studentID = studentid
    new_usr.name = name
    new_usr.password = password
    new_usr.email = email
    new_usr.save()
    return render(request, "login_manage/add_to_db.html")


# python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
def GenPassword(length=8, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


#  忘记密码发送邮件
def sendemail(request):
    studentID_target = request.GET.get("studentID")
    email_target = request.GET.get("email")
    find = models.User.objects.filter(studentID=studentID_target, email=email_target)
    if not find:
        message = "notequal"
        return HttpResponse(json.dumps({"message": message}))
    pawdtemp = GenPassword(8)
    send_mail(
        subject=u"这是新的密码,请使用新的密码登录", message=pawdtemp,
        from_email='18210714886@163.com', recipient_list=[email_target], fail_silently=False,
    )
    new_pwd_usr = models.User.objects.get(email=email_target)
    new_pwd_usr.password = pawdtemp
    new_pwd_usr.save()
    message = "equal"
    return HttpResponse(json.dumps({"message": message}))


# 显示用户信息
def user_info(request):
    if not request.session.get('studentID'):
        request.session.flush()
        return redirect('/login/')
    print("sdfsdfsa")
    studentid = request.session.get('studentID')
    stu = models.User.objects.get(studentID=studentid)
    return render(request, "login_manage/user_info.html", locals())


# 更新用户信息
def update_user(request):
    studentid = request.GET.get("studentid")
    citynum = request.GET.get("citynum")
    city = request.GET.get("city")
    address = request.GET.get("address")
    zipcode = request.GET.get("zipcode")
    telephone = request.GET.get("telephone")
    qq = request.GET.get("qq")
    stu = models.User.objects.get(studentID=studentid)
    stu.city = city
    stu.detail_address = address
    stu.zip_code = zipcode
    stu.telephone = telephone
    stu.qq = qq
    stu.city_num = citynum
    stu.save()
    return render(request, "login_manage/update_user.html")
