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

class FoundRecordModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:

        model = models.FoundRecord
        exclude = ["username"]
def found_list(request):
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

    return render(request,"user_found_list.html",context)

def found_record_list(request):
    data_dict = {}
    value = request.GET.get("q", "")
    if value:
        data_dict["thing__contains"] = value
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