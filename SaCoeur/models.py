from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class building(models.Model):
    name = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    capacity = models.IntegerField()
    type = models.IntegerField(choices=((1, 'Storage'),
                                        (2, 'Store')),
                               default=1)

    def __str__(self):
        return self.name


class product_description(models.Model):
    reference = models.CharField(max_length=120)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    color = models.CharField(max_length=20)





class product(models.Model):
    arrival_date = models.DateField()
    id_building = models.ForeignKey(
        'building',
         models.SET_NULL,
         blank=False,
         null=True)
    id_product_description = models.ForeignKey('product_description')


    def avaibility(self):
        if not product.id_building:
            return False

