import json

from django.forms import ModelForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import datetime
from Admin_app import models

import pandas as pd


class FoundModelForm(ModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:
        model = models.Found
        exclude = ["username"]
class LostModelForm(ModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:
        model = models.Lost
        exclude = ["username"]
def chart_index(request):
    fount_list = models.Found.objects.filter().order_by("found_time")# 遗留列表
    lost_list = models.Lost.objects.filter().order_by("lost_time")# 挂失列表

    # 丢失物品排名
    thing_list = []
    found_queryset = models.Found.objects.filter()
    for i in found_queryset:
        thing_list.append([str(i.thing), str(i.sort)])
    found_record_queryset = models.FoundRecord.objects.filter().all()
    for i in found_record_queryset:
        thing_list.append([str(i.thing), str(i.sort)])
    df = pd.DataFrame(thing_list)
    df = df.value_counts()
    thing = []
    n = 1
    for i in df.index[:5]:
        thing.append({"ti":n,"th":i[0],"so":i[1],"co":df[i]})
        # thing.append([n,i[0],i[1],df[i].astype("float")])
        n += 1
    context = {
        "fount_list":fount_list,# 遗留列表
        "lost_list":lost_list,# 挂失列表
        "thing": thing,
    }
    return render(request,"index.html",context)


def chart_resouse(request):
    # 累计今日挂失
    today_lost_count = models.Lost.objects.filter(lost_time=datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")[:10]).count()  # 今日挂失
    today_lost_record_count = models.LostRecord.objects.filter(lost_time=datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")[:10]).count()  # 今日挂失
    today_lost_all = today_lost_count + today_lost_record_count  # 累计今日挂失

    # 累计所有挂失
    all_lost_count = models.Lost.objects.filter().count()
    all_lost_record_count = models.LostRecord.objects.filter().count()
    all_lost_all = all_lost_count + all_lost_record_count
    # 累计今日遗留
    today_found_count = models.Found.objects.filter(found_time=datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")[:10]).count()  # 今日遗留
    today_found_record_count = models.FoundRecord.objects.filter(found_time=datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")[:10]).count()  # 今日遗留
    today_found_all = today_found_count + today_found_record_count
    # 累计所有遗留
    all_found_count = models.Found.objects.filter().count()
    all_found_record_count = models.FoundRecord.objects.filter().count()
    all_found_all = all_found_count + all_found_record_count

    context = {
        "today_lost_all": today_lost_all,  # 今日挂失
        "all_lost_all": all_lost_all,  # 累计挂失
        "today_found_all": today_found_all,  # 今日遗留
        "all_found_all": all_found_all,  # 累计遗留
        "all_lost_count": all_lost_count,  # 未还挂失
        "all_found_count": all_found_count,  # 未还遗留


    }
    return JsonResponse(context)

def chart_location(request):
    # 遗失位置分析
    location_list = []
    location_dict = {}
    found_queryset = models.Found.objects.filter()
    for i in found_queryset:
        location_list.append(str(i.location))
    found_record_queryset = models.FoundRecord.objects.filter().all()
    for i in found_record_queryset:
        location_list.append(str(i.location))
    for i in location_list:
        location_dict[i] = location_dict.get(i,0) + 1

    context = {
        # 位置数据
        "location_key" : list(location_dict.keys()),
        "location_value" : list(location_dict.values())
        # "location_key" : "123",
        # "location_value" : 10
    }
    return JsonResponse(context)

def chart_sort(request):

    # 遗失种类分析
    sort_list = []
    sort_dict = {}
    found_queryset = models.Found.objects.filter()
    for i in found_queryset:
        sort_list.append(str(i.sort))
    found_record_queryset = models.FoundRecord.objects.filter().all()
    for i in found_record_queryset:
        sort_list.append(str(i.sort))
    for i in sort_list:
        sort_dict[i] = sort_dict.get(i, 0) + 1
    data = []
    for i in sort_dict:
        data.append({"name": i,"value":sort_dict[i]})

    context = {
        "data":data,
        "legend":[i["name"] for i in data]
    }
    return JsonResponse({"context":context})

def chart_time(request):
    # 时间数据

    def queryset_count(day):
        lost_count = models.Lost.objects.filter(lost_time=day).count()+models.LostRecord.objects.filter(lost_time=day).count() # 挂失数量
        found_count = models.Found.objects.filter(found_time=day).count()+models.FoundRecord.objects.filter(found_time=day).count() # 遗留数量
        return lost_count,found_count

    today = datetime.date.today()  # 今天时间
    oneday = datetime.timedelta(days=1)  # 时间间隔

    day_list = []
    lost_count_list = []
    found_count_list = []
    for i in range(12):
        day = today-i*oneday
        lost_temp,found_temp = queryset_count(day)
        day_list.append(day)
        lost_count_list.append(lost_temp)
        found_count_list.append(found_temp)
    context = {
        "day_list" : day_list,
        "lost_count_list":lost_count_list,
        "found_count_list":found_count_list

    }

    return JsonResponse(context)



