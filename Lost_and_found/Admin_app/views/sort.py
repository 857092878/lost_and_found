from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django import forms
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
# Create your views here.
from Admin_app.utils.pagination import Pagination


class SortModelForm(BootStrapModelForm):
    class Meta:
        model = models.Sort
        fields = "__all__"

def sort_list(request):
    """种类列表"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    queryset = models.Sort.objects.all()
    page_object = Pagination(request, queryset)
    form = SortModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request,"sort_list.html",context)
def sort_delete(request):
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
    exists = models.Sort.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    models.Sort.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def sort_add(request):
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
        form = SortModelForm()
        return render(request, "add.html", {'form': form,'title':'新建分类'})
    # 用户post提交数据后，数据校验
    form = SortModelForm(data=request.POST)
    if form.is_valid():
        form.save()  # 保存数据库
        return redirect("/sort/list/")
    return render(request, "add.html", {'form': form, 'title': '新建分类'})

def sort_edit(request,nid):
    """种类"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    row_object = models.Sort.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行
        form = SortModelForm(instance=row_object)  # 默认显示出来

        return render(request, "edit.html", {'form': form})
    form = SortModelForm(data=request.POST, instance=row_object)  # 不用新增一个数据，直接代替代替代替
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要在用户输入意外的一点值
        # form.instance.字段名 = 值
        form.save()  # 保存数据库
        return redirect("/sort/list/")
        # 检验失败
    return render(request, "edit.html", {"form":form,"title":"种类编辑"})