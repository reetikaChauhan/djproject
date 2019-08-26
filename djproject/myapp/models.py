from django.db import models

# Create your models here.
class web1(models.Model):
    news_head = models.CharField(max_length=255)
    news_web = models.CharField(max_length=255)
    news_img = models.CharField(max_length=255)
    date = models.DateField()


class News(models.Model):
    title = models.CharField(max_length=225)
    authors = models.CharField(max_length=225)
    publisher = models.ForeignKey(web1,on_delete=models.PROTECT)
    publication_date = models.DateField()


class tb_registration(models.Model):
    name= models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)
class employee(models.Model):
    #ename = models.CharField(max_length=225)
    email1 = models.ForeignKey(tb_registration, on_delete=models.PROTECT)
    Job_title = models.CharField(max_length=225)
    Specialization = models.CharField(max_length=225)
    experience = models.CharField(max_length=225)








