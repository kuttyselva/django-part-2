from django.db import models

# Create your models here.
class Topic(models.Model):
    top=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top

class Exe(models.Model):

    fname=models.CharField('First name',max_length=264,unique=True)
    lname=models.CharField('Last name',max_length=264,unique=True)
    email = models.EmailField('Email',max_length=70,blank=True, null= True, unique= True)
    def __str__(self):
        return self.fname


class Webpage(models.Model):
    topic =models.ForeignKey(Topic,on_delete=models.DO_NOTHING,)
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=False)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.DO_NOTHING)
    date=models.DateField()

    def __str__(self):
        return str(self.date)
