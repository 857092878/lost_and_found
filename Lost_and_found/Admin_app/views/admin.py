from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django import forms
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
# Create your views here.
from Admin_app.utils.encrypt import md5
from Admin_app.utils.pagination import Pagination


class AdminModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["username"]

def admin_list(request):
    """种类列表"""
    data_dict = {}
    value = request.GET.get("q", "")
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    if value:
        data_dict["thing__contains"] = value
    queryset = models.Admin.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)
    form = AdminModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request,"admin_list.html",context)

def admin_delete(request):
    """种类"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    uid = request.GET.get("uid")
    exists = models.Admin.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    models.Admin.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

class AdminAddModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码",
                                       widget=forms.PasswordInput(render_value=True))
    class Meta:

        model = models.Admin
        fields = ["username","password","confirm_password"]
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

def admin_add(request):
    """种类"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    if request.method == "GET":
        form = AdminAddModelForm()
        return render(request, "add.html", {'form': form,'title':'新建管理员'})
    # 用户post提交数据后，数据校验
    form = AdminAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()  # 保存数据库
        return redirect("/admin/list/")
    return render(request, "add.html", {'form': form, 'title': '新建管理员'})


# 重置密码
class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码",
                                       widget=forms.PasswordInput(render_value=True))#密码不清空
    class Meta:

        model = models.Admin
        fields = ["password","confirm_password"]
        widgets = {
            "password":forms.PasswordInput(render_value=True)
        }
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        # 去数据库校验
        exists = models.Admin.objects.filter(id=self.instance.pk,password=md5_pwd).exists()
        # instance为一参数，需要传递，instance.pk为参数的id，,password=md5_pwd为比对的新数据，如果没有id默认为数据库中的所有字段数据比对，如有id则为一条id比对

        if exists:
            raise forms.ValidationError("密码不能与之前的一致")
        return md5(pwd)#加密

    def clean_confirm_password(self):
        """cleaned_data为request POST请求到的数据，此处为请求到的confirm_password数据"""
        print(self.cleaned_data)
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise forms.ValidationError("密码不一致，请重新输入")
        return confirm


def admin_reset(request,nid):
    """重置密码"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/admin/list/")
    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request,"edit.html",{"title":title,"form":form})
    form = AdminResetModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "edit.html", {"title": title, "form": form})