from django.db import models

# Create your models here.


class Product(models.Model):
    code = models.CharField(verbose_name="Product Code", max_length=10, unique=True)
    name = models.CharField(verbose_name="Product Name", max_length=50)

    def __str__(self):
        return self.name


class Frame(models.Model):
    name = models.CharField(verbose_name="Frame Name", max_length=50)

    def __str__(self):
        return self.name


class Length(models.Model):
    name = models.CharField(verbose_name="Length", max_length=50)

    def __str__(self):
        return self.name


class Coat(models.Model):
    name = models.CharField(verbose_name="Coating Name", max_length=50)

    def __str__(self):
        return self.name


class Shutter(models.Model):
    name = models.CharField(verbose_name="Shutter Name", max_length=50)

    def __str__(self):
        return self.name


class Ilpatti(models.Model):
    name = models.CharField(verbose_name="I/l Patti Name", max_length=50)

    def __str__(self):
        return self.name


class Uchannel(models.Model):
    name = models.CharField(verbose_name="Uchannel Name", max_length=50)

    def __str__(self):
        return self.name


class Glass(models.Model):
    name = models.CharField(verbose_name="Glass Name", max_length=50)

    def __str__(self):
        return self.name


class Mnet(models.Model):
    name = models.CharField(verbose_name="Mosquito Net Name", max_length=50)

    def __str__(self):
        return self.name


class Clip(models.Model):
    name = models.CharField(verbose_name="Clip Name", max_length=50)

    def __str__(self):
        return self.name


class Addon(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT, verbose_name="Product Name")
    item = models.CharField(verbose_name="Item Name", max_length=50)
    nos = models.CharField(verbose_name="Item Name", max_length=50)
    rate = models.FloatField(verbose_name="Rate")

    def __str__(self):
        return self.item

