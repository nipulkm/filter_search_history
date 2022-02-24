from django.db import models

class User(models.Model):
    user_ip_address = models.CharField(max_length=39, unique=True)

class Keyword(models.Model):
    word = models.CharField(max_length=255, unique=True)

class Result(models.Model):
    search_result = models.CharField(max_length=255, unique=True)
    keyword = models.ForeignKey(Keyword, on_delete=models.PROTECT)

class History(models.Model):
    time = models.TimeField(auto_now=True, auto_now_add=False)
    date = models.DateField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    keyword = models.ForeignKey(Keyword, on_delete=models.PROTECT)