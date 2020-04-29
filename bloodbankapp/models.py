from django.db import models

# Create your models here.
class donate(models.Model):
    name=models.CharField(max_length=300,null=True,blank=True)
    fathername=models.CharField(max_length=300,null=True,blank=True)
    hospital=models.CharField(max_length=300,null=True,blank=True)
    group=models.CharField(max_length=300,null=True,blank=True)
    email=models.CharField(max_length=300,null=True,blank=True)
    phone=models.CharField(max_length=300,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
            return self.group


class addhospital(models.Model):
    hospital=models.CharField(max_length=400,null=True ,blank=True)
    address=models.CharField(max_length=400,null=True ,blank=True)
    phone=models.CharField(max_length=400,null=True ,blank=True)
    def __str__(self):
        return self.hospital

class bloodrequest(models.Model):
    name=models.CharField(max_length=400,null=True ,blank=True)
    fathername=models.CharField(max_length=400,null=True ,blank=True)
    group=models.CharField(max_length=400,null=True ,blank=True)
    email=models.CharField(max_length=400,null=True ,blank=True)
    phone=models.CharField(max_length=400,null=True ,blank=True)
    address=models.CharField(max_length=400,null=True ,blank=True)
    def __str__(self):
        return self.name