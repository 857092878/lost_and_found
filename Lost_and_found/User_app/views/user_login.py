from django.shortcuts import render,HttpResponse,redirect
from django import forms
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapForm
from Admin_app.utils.encrypt import md5
from Admin_app.utils.code import check_code
from io import BytesIO

class LoginForm(BootStrapForm):
    username = forms.CharField(label="用户名",
                               widget=forms.TextInput,
                               required=True#必须得填写
                               )
    password = forms.CharField(label="密码",
                               widget=forms.PasswordInput(render_value=True),#只给一个表单设置，错误则不会清零
                               required = True#必须得填写
                               )
    code = forms.CharField(label="验证码",
                           widget=forms.TextInput,  # 只给一个表单设置，错误则不会清零
                           required=True  # 必须得填写
                               )
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


# class LoginModeForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         fields = ["username","password"]

def login(request):
    """登陆"""
    if request.method == "GET":
        form = LoginForm()
        return render(request,"user_login.html",{"form":form,"title":"用户登陆"})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 验证成功
        # 取数据库校验用户名和密码是否正确
        # admin_object = models.Admin.objects.filter(username="XXX",password="XXX").first()
        # 验证码的校验
        user_input_code = form.cleaned_data.pop("code")#去除输入的验证码的同时并删除改验证码防止与数据库校验时报错
        code = request.session.get("image_code","")#设置的正确的验证码，但有60S的存在时间，此处的image_code为web上的image_code
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, "user_login.html", {"form": form,"title":"用户登陆"})

        user_object = models.User.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error("password","用户名或密码错误")
            return render(request, "user_login.html", {"form": form,"title":"用户登陆"})
        # 用户名和密码正确
        # 网站随机生成字符串；写到用户浏览器的cookie中，在写入到session中
        request.session["info"] = {'user_id': user_object.id, 'user_name': user_object.username}#操作的是电脑上的cookies
        request.session.set_expiry(60*60*24)#如果登陆成功，重新设置超时时间,7天不用验证码，免登录

        # return redirect("/found/list/")
        return redirect("/user/mylost/")

    return render(request,"user_login.html",{"form":form,"title":"用户登陆"})

def logout(request):
    """注销"""

    request.session.clear()# 清除当前的session
    return redirect("/user/login/")


def image_code(request):
    """生成图片验证码"""
    # 调用pillow函数，生成图片
    img,code_string = check_code()
    # 写入到自己的session中，以便于后续获取验证码再进行校验
    request.session["image_code"] = code_string
    # 在Session设置超时
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream,"png")
    stream.getvalue()
    return HttpResponse(stream.getvalue())

