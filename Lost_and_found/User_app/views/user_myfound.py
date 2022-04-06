from django.http import JsonResponse
from django.shortcuts import render, redirect
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
from Admin_app import models
from Admin_app.utils.pagination import Pagination


class FoundModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:

        model = models.Found
        exclude = ["username"]
def found_list(request):
    data_dict = {}
    value = request.GET.get("q", "")
    my_id = request.session["info"]["user_name"]
    if value:
        data_dict["thing__contains"] = value
    data_dict["username__contains"] = my_id
    queryset = models.Found.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset)
    form = FoundModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value":value
    }

    return render(request,"user_myfound.html",context)

def found_add(request):
    """上传文件"""
    title = "捡到东西"

    if request.method == "GET":
        form = FoundModelForm()
        return render(request, "found_upload.html", {"form":form, "title":title})
    form = FoundModelForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        form.instance.username = request.session["info"]["user_name"]
        form.save()
        return redirect("/user/myfound/")
    return render(request, "user_found_upload.html", {"form": form, "title": title})

def found_delete(request):
    """挂失撤回"""
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
                                username=queryset.username,
                                link=queryset.link,
                                description=queryset.description
                                )
    models.Found.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def found_edit(request,nid):
    """种类"""
    row_object = models.Found.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行
        form = FoundModelForm(instance=row_object)  # 默认显示出来

        return render(request, "user_found_edit.html", {"form":form,"title":"更改信息"})
    form = FoundModelForm(data=request.POST, files=request.FILES,instance=row_object)  # 不用新增一个数据，直接代替代替代替
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要在用户输入意外的一点值
        # form.instance.字段名 = 值
        form.instance.username = request.session["info"]["user_name"]
        form.save()  # 保存数据库
        return redirect("/user/myfound/")
        # 检验失败
    return render(request, "user_found_edit.html", {"form":form,"title":"更改信息"})
def found_cancel(request,nid):
    """种类"""
    models.Found.objects.filter(id=nid).delete()
    return redirect("/user/mylost/")