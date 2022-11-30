from django.db import models

class Product(models.Model):
    productno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=False)
    price=models.FloatField(null=False)

    def __repr__(self):
        return str({'productno':self.productno,'name':self.name,'price':self.price})