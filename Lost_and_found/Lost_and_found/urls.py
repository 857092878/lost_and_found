"""Lost_and_found URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from django.urls import path
from Admin_app.views import sort,location,admin,lost,found,found_record,lost_record,user,admin_login
from Chart_app.views import chart
from User_app.views import user_login, user_mylost, user_mylost_record, user_myfound, user_myfound_record, lost_list, \
    found_list, register

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 配置动态文件夹
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 管理员页面

    # 种类管理
    path('sort/list/', sort.sort_list),# 显示列表
    path('sort/delete/', sort.sort_delete),# 删除
    path('sort/add/', sort.sort_add),# 添加
    path('sort/<int:uid>/edit/', sort.sort_edit),# 编辑

    # 地点管理
    path('location/list/', location.location_list),# 显示列表
    path('location/delete/', location.location_delete),# 删除
    path('location/add/', location.location_add),# 添加
    path('location/<int:nid>/edit/', location.location_edit),# 编辑

    # 管理员管理
    path('admin/list/', admin.admin_list),# 显示列表
    path('admin/delete/', admin.admin_delete),# 删除
    path('admin/add/', admin.admin_add),# 添加
    path('admin/<int:nid>/edit/', admin.admin_reset),# 编辑

    # 用户管理
    path('user/list/', user.user_list),# 显示列表
    path('user/delete/', user.user_delete),# 删除
    path('user/add/', user.user_add),# 添加
    path('user/<int:nid>/edit/', user.user_reset),# 编辑

    #挂失列表
    path("lost/list/", lost.lost_list),
    path("lost/add/", lost.lost_add),
    path("lost/delete/", lost.lost_delete),
    path("lost/<int:nid>/edit/", lost.lost_edit),
    path("lost/<int:nid>/cancel/", lost.lost_cancel),

    #遗留列表
    path("found/list/", found.found_list),
    path("found/add/", found.found_add),
    path("found/delete/", found.found_delete),
    path("found/<int:nid>/edit/", found.found_edit),
    path("found/<int:nid>/cancel/", found.found_cancel),

    # 遗留记录
    path("found/record/list/", found_record.found_record_list),
    path("found/record/delete/", found_record.found_record_delete),

    # 挂失记录
    path("lost/record/list/", lost_record.lost_record_list),
    path("lost/record/delete/", lost_record.lost_record_delete),

    # 管理员登陆
    path('admin/login/', admin_login.login),# 登陆
    path('admin/logout/', admin_login.logout),# 注销
    path('image/code/', admin_login.image_code),# 图片验证码

    # 用户界面
    path('user/login/', user_login.login),# 登陆
    path('user/logout/', user_login.logout),# 注销

    # 我的挂失
    path('user/mylost/', user_mylost.lost_list),# 我的挂失；列表
    path("user/mylost/add/", user_mylost.lost_add),
    path("user/mylost/delete/", user_mylost.lost_delete),
    path("user/mylost/<int:nid>/edit/", user_mylost.lost_edit),
    path("user/mylost/<int:nid>/cancel/", user_mylost.lost_cancel),

    # 我的挂失记录
    path('user/mylost/record/', user_mylost_record.lost_record_list),# 我的挂失记录
    path("user/mylost/record/delete/", user_mylost_record.lost_record_delete),

    # # 我捡到的
    path('user/myfound/', user_myfound.found_list),  # 我的挂失；列表
    path("user/myfound/add/", user_myfound.found_add),
    path("user/myfound/delete/", user_myfound.found_delete),
    path("user/myfound/<int:nid>/edit/", user_myfound.found_edit),
    path("user/myfound/<int:nid>/cancel/", user_myfound.found_cancel),

    # # 我捡到的
    path('user/myfound/record/', user_myfound_record.found_record_list),  # 我的挂失记录
    path("user/myfound/record/delete/", user_myfound_record.found_record_delete),

    # 挂失列表
    path("user/lost/list/", lost_list.lost_list),
    path("user/lost/record/list/", lost_list.lost_record_list),

    # 遗失列表
    path("user/found/list/", found_list.found_list),
    path("user/found/record/list/", found_list.found_record_list),

    # 用户注册
    path("user/register/", register.user_register),

    # 可视化
    path("chart/index/", chart.chart_index),
    path("chart/index/resouse/", chart.chart_resouse),# 资源分析
    path("chart/index/location/", chart.chart_location),# 位置分析
    path("chart/index/sort/", chart.chart_sort),# 种类分析
    path("chart/index/time/", chart.chart_time),# 种类分析


]
