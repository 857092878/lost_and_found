import random
from datetime import datetime

from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
from Admin_app import models
from Admin_app.utils.encrypt import md5
from Admin_app.utils.pagination import Pagination
class UserAddModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码",
                                       widget=forms.PasswordInput(render_value=True))
    class Meta:

        model = models.User
        fields = ["password","confirm_password"]
        widgets = {
            "password":forms.PasswordInput
        }
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)#加密

    def clean_confirm_password(self):
        """cleaned_data为request POST请求到的数据，此处为请求到的confirm_password数据"""
        print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise forms.ValidationError("密码不一致，请重新输入")
        return confirm
def user_register(request):
    """用户注册"""
    if request.method == "GET":
        form = UserAddModelForm()
        return render(request, "user_register.html", {'form': form})

    # 用户post提交数据后，数据校验
    form = UserAddModelForm(data=request.POST)
    password = request.POST.get("confirm_password")
    if form.is_valid():
        form.instance.username = datetime.now().strftime("%Y%m%d%H%M%S")[2:-2] + str(random.randint(100,999))
        username = form.instance.username
        form.save()  # 保存数据库
        return render(request,"success.html",{"username":username,"password":password})
    return render(request, "user_register.html", {'form': form})