from django.http import JsonResponse
from django.shortcuts import render, redirect
from Admin_app import models
from Admin_app.utils.bootstrap import BootStrapModelForm
from Admin_app import models
from Admin_app.utils.pagination import Pagination


class FoundRecordModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:

        model = models.FoundRecord
        fields = "__all__"
def found_record_list(request):
    data_dict = {}
    value = request.GET.get("q", "")
    my_id = request.session["info"]["user_name"]
    if value:
        data_dict["thing__contains"] = value
    data_dict["username__contains"] = my_id
    queryset = models.FoundRecord.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset)
    form = FoundRecordModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value":value
    }
    return render(request,"user_found_record.html",context)

def found_record_delete(request):
    """挂失撤回"""
    uid = request.GET.get("uid")
    exists = models.FoundRecord.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    queryset = models.FoundRecord.objects.filter(id=uid).first()
    models.Found.objects.create(
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
    models.FoundRecord.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})

