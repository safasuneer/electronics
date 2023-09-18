from django.db import models

# Create your models here.

class serviceproductcollection(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    product=models.CharField(max_length=500)
    productlocation=models.CharField(max_length=500)
    issueofproduct=models.CharField(max_length=500)
    duration=models.CharField(max_length=500)

class shops(models.Model):
    shopname=models.CharField(max_length=500)
    shoplocation=models.CharField(max_length=500)
    phone=models.ImageField()
    duration=models.CharField(max_length=500)
    price=models.IntegerField()



class serviceamount(models.Model):
    price=models.IntegerField()
    description=models.CharField(max_length=500)


class productdetails(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    product=models.CharField(max_length=500)
    productlocation=models.CharField(max_length=500)
    pickoutlocation=models.CharField(max_length=500)
    pickupdate=models.DateField(null=True)



class paymentdetails(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    price=models.ForeignKey(serviceamount,on_delete=models.CASCADE)
    product=models.CharField(max_length=500)
    productlocation=models.CharField(max_length=500)
    pickoutlocation=models.CharField(max_length=500)
    pickupdate=models.DateField(null=True)
    pickoutdate=models.DateField(null=True)




    
    