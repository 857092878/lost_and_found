from django.http import JsonResponse
from django.shortcuts import render, redirect
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
from Admin_app import models
from Admin_app.utils.pagination import Pagination


class LostModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:

        model = models.Lost
        # fields = "__all__"
        exclude = ["username"]
def lost_list(request):
    data_dict = {}
    value = request.GET.get("q", "")
    my_id = request.session["info"]["user_name"]
    if value:
        data_dict["thing__contains"] = value
    data_dict["username__contains"] = my_id
    queryset = models.Lost.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset)
    form = LostModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value":value
    }

    return render(request,"user_mylost.html",context)

def lost_add(request):
    """上传文件"""
    title = "挂失"

    if request.method == "GET":
        form = LostModelForm()
        return render(request, "lost_upload.html", {"form":form, "title":title})
    form = LostModelForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        form.instance.username = request.session["info"]["user_name"]
        form.save()
        return redirect("/user/mylost/")
    return render(request, "user_lost_upload.html", {"form": form, "title": title})

def lost_delete(request):
    """挂失撤回"""
    uid = request.GET.get("uid")
    exists = models.Lost.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    queryset = models.Lost.objects.filter(id=uid).first()
    models.LostRecord.objects.create(
                                img=queryset.img,
                                thing=queryset.thing,
                                sort_id=queryset.sort.id,
                                location_id=queryset.location.id,
                                lost_time=queryset.lost_time,
                                name=queryset.name,
                                username=queryset.username,
                                link=queryset.link,
                                description=queryset.description
                                )
    models.Lost.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

def lost_edit(request,nid):
    """种类"""
    row_object = models.Lost.objects.filter(id=nid).first()
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行
        form = LostModelForm(instance=row_object)  # 默认显示出来

        return render(request, "user_lost_edit.html", {'form': form})
    form = LostModelForm(data=request.POST, files=request.FILES,instance=row_object)  # 不用新增一个数据，直接代替代替代替
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要在用户输入意外的一点值
        # form.instance.字段名 = 值
        form.instance.username = request.session["info"]["user_name"]
        form.save()  # 保存数据库
        return redirect("/user/mylost/")
        # 检验失败
    return render(request, "user_lost_edit.html", {"form":form,"title":"挂失编辑"})
def lost_cancel(request,nid):
    """种类"""
    models.Lost.objects.filter(id=nid).delete()
    return redirect("/user/mylost/")