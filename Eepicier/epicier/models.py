from django.db import models

# Create your models here.
class Client (models.Model):
    firstName = models.CharField(max_length=190,null=True)
    lastName = models.CharField(max_length=190,null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=190,null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.lastName
    
class Produit (models.Model):
    status=(('shirt','shirt'),('t-shirt','t-shirt'),('jeans','jeans'),('shoes','shoes'))
    title = models.CharField(max_length=190,null=True)
    price= models.FloatField(null=True)
    description = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,null=True,choices=status)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    
class Credit (models.Model):
    STATUS = (('unpaid','unpaid'),('paid','paid'))
    client = models.ForeignKey(Client,null=True,on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,null=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=200,null=True,choices=STATUS,default="unpaid")
    date_created = models.DateTimeField(auto_now_add=True,null=True)