from django.db import models

# Create your models here.

class Sort(models.Model):
    '''种类表'''
    title = models.CharField(verbose_name="种类",max_length=32)
    def __str__(self):
        return self.title

class Location(models.Model):
    '''地点'''
    title = models.CharField(verbose_name="地点",max_length=32)
    def __str__(self):
        return self.title

class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=32)
    def __str__(self):
        return self.username

class User(models.Model):
    """用户"""
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=32)
    def __str__(self):
        return self.username

class Lost(models.Model):
    """失主"""
    img = models.FileField(verbose_name="照片", max_length=128, upload_to='lost/')
    thing = models.CharField(verbose_name="掉的物品", max_length=32)
    sort = models.ForeignKey(verbose_name="种类", to="Sort",to_field="id", on_delete=models.CASCADE)
    location = models.ForeignKey(verbose_name="掉的位置", to="Location",to_field="id", on_delete=models.CASCADE)
    lost_time = models.DateField(verbose_name="掉的时间")
    name = models.CharField(verbose_name="失主姓名", max_length=32)
    username = models.CharField(verbose_name="用户名", max_length=32,default="null")
    link = models.CharField(verbose_name="失主联系方式/(QQ/微信)", max_length=11)
    description = models.TextField(verbose_name="描述",max_length=64)

class Found(models.Model):
    """拾主"""
    img = models.FileField(verbose_name="照片", max_length=128, upload_to='lost/')
    thing = models.CharField(verbose_name="捡的物品", max_length=32)
    sort = models.ForeignKey(verbose_name="种类", to="Sort",to_field="id", on_delete=models.CASCADE)
    location = models.ForeignKey(verbose_name="捡的位置", to="Location",to_field="id", on_delete=models.CASCADE)
    found_time = models.DateField(verbose_name="捡的时间")
    name = models.CharField(verbose_name="拾主姓名", max_length=32)
    username = models.CharField(verbose_name="用户名", max_length=32,default="null")
    link = models.CharField(verbose_name="拾主联系方式/(QQ/微信)", max_length=11)
    description = models.TextField(verbose_name="描述",max_length=64)

class FoundRecord(models.Model):
    """遗失记录"""
    img = models.FileField(verbose_name="照片", max_length=128, upload_to='lost/')
    thing = models.CharField(verbose_name="捡的物品", max_length=32)
    sort = models.ForeignKey(verbose_name="种类", to="Sort",to_field="id", on_delete=models.CASCADE)
    location = models.ForeignKey(verbose_name="捡的位置", to="Location",to_field="id", on_delete=models.CASCADE)
    found_time = models.DateField(verbose_name="捡的时间")
    name = models.CharField(verbose_name="拾主姓名", max_length=32)
    username = models.CharField(verbose_name="用户名", max_length=32,default="null")
    link = models.CharField(verbose_name="拾主联系方式/(QQ/微信)", max_length=11)
    description = models.TextField(verbose_name="描述",max_length=64)

class LostRecord(models.Model):
    """挂失记录"""
    img = models.FileField(verbose_name="照片", max_length=128, upload_to='lost/')
    thing = models.CharField(verbose_name="掉的物品", max_length=32)
    sort = models.ForeignKey(verbose_name="种类", to="Sort",to_field="id", on_delete=models.CASCADE)
    location = models.ForeignKey(verbose_name="掉的位置", to="Location",to_field="id", on_delete=models.CASCADE)
    lost_time = models.DateField(verbose_name="掉的时间")
    name = models.CharField(verbose_name="失主姓名", max_length=32)
    username = models.CharField(verbose_name="用户名", max_length=32,default="null")
    link = models.CharField(verbose_name="失主联系方式/(QQ/微信)", max_length=11)
    description = models.TextField(verbose_name="描述",max_length=64)


