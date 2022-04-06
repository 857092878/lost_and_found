from django.http import JsonResponse
from django.shortcuts import render, redirect
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
from Admin_app import models
from django import forms

from Admin_app.utils.pagination import Pagination


class FoundModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:

        model = models.Found
        fields = "__all__"

def found_list(request):
    """遗列表"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    data_dict = {}
    value = request.GET.get("q", "")
    if value:
        data_dict["thing__contains"] = value
    queryset = models.Found.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset)
    form = FoundModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value":value
    }
    return render(request,"found_list.html",context)

def found_add(request):
    """上传文件"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    title = "捡到东西"

    if request.method == "GET":
        form = FoundModelForm()
        return render(request, "found_upload.html", {"form":form, "title":title})
    form = FoundModelForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/found/list/")
    return render(request, "found_upload.html", {"form": form, "title": title})

def found_delete(request):
    """挂失撤回"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    uid = request.GET.get("uid")
    exists = models.Found.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    queryset = models.Found.objects.filter(id=uid).first()
    models.FoundRecord.objects.create(
                                img=queryset.img,
                                thing=queryset.thing,
                                sort_id=queryset.sort.id,
                                location_id=queryset.location.id,
                                found_time=queryset.found_time,
                                name=queryset.name,
                                link=queryset.link,
                                description=queryset.description
                                )
    models.Found.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def found_edit(request,nid):
    """种类"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    row_object = models.Found.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行
        form = FoundModelForm(instance=row_object)  # 默认显示出来

        return render(request, "found_edit.html", {'form': form})
    form = FoundModelForm(data=request.POST, instance=row_object)  # 不用新增一个数据，直接代替代替代替
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要在用户输入意外的一点值
        # form.instance.字段名 = 值
        form.save()  # 保存数据库
        return redirect("/found/list/")
        # 检验失败
    return render(request, "found_edit.html", {"form":form,"title":"挂失编辑"})

def found_cancel(request,nid):
    """种类"""
    try:
        id = request.session["info"]["admin_id"]
        username = request.session["info"]["admin_name"]
        exists = models.Admin.objects.filter(id=id, username=username).exists()
        print("管理员登陆成功")
    except:
        print("管理员登陆失败")
        return redirect("/admin/login/")
    models.Found.objects.filter(id=nid).delete()
    return redirect("/found/list/")