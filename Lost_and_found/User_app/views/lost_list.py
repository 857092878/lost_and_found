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
class LostRecordModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:

        model = models.LostRecord
        exclude = ["username"]

def lost_list(request):
    data_dict = {}
    value = request.GET.get("q", "")
    if value:
        data_dict["thing__contains"] = value
    queryset = models.Lost.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset)
    form = LostModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value":value
    }

    return render(request,"user_lost_list.html",context)

def lost_record_list(request):
    data_dict = {}
    value = request.GET.get("q", "")
    if value:
        data_dict["thing__contains"] = value
    queryset = models.LostRecord.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset)
    form = LostRecordModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value":value
    }
    return render(request,"user_lost_record_list.html",context)