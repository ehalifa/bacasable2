from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    capacity = models.IntegerField()
    type = models.IntegerField(choices=((1, 'Storage'),
                                        (2, 'Store')),
                               default=1)

    def __str__(self):
        return self.name


class Product_Description(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=25)
    reference = models.CharField(max_length=120)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name




class Product(models.Model):
    arrival_date = models.DateField()
    id_building = models.ForeignKey(
        Building,
         models.SET_NULL,
         blank=True,
         null=True)
    id_product_description = models.ForeignKey(Product_Description)

    def __str__(self):
        return self.id_product_description.name

    def avaibility(self):
        if not Product.id_building:
            return False

