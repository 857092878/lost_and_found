from django.http import JsonResponse
from django.shortcuts import render, redirect
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
from Admin_app import models
from Admin_app.utils.pagination import Pagination


class LostRecordModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:

        model = models.LostRecord
        fields = "__all__"
def lost_record_list(request):
    data_dict = {}
    value = request.GET.get("q", "")
    my_id = request.session["info"]["user_name"]
    if value:
        data_dict["thing__contains"] = value
    data_dict["username__contains"] = my_id
    queryset = models.LostRecord.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset)
    form = LostRecordModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value":value
    }
    return render(request,"user_lost_record.html",context)

def lost_record_delete(request):
    """挂失撤回"""
    uid = request.GET.get("uid")
    exists = models.LostRecord.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    queryset = models.LostRecord.objects.filter(id=uid).first()
    models.Lost.objects.create(
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
    models.LostRecord.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

