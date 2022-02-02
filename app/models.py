from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name="Product Name",max_length=50)

    def __str__(self):
        return self.name

class Frame(models.Model):
    name = models.CharField(verbose_name="Frame Name",max_length=50)

    def __str__(self):
        return self.name

class Length(models.Model):
    name = models.CharField(verbose_name="Length",max_length=50)

    def __str__(self):
        return self.name

class Coat(models.Model):
    name = models.CharField(verbose_name="Coating Name",max_length=50)

    def __str__(self):
        return self.name

class Shutter(models.Model):
    name = models.CharField(verbose_name="Shutter Name",max_length=50)

    def __str__(self):
        return self.name

class Ilpatti(models.Model):
    name = models.CharField(verbose_name="I/l Patti Name",max_length=50)

    def __str__(self):
        return self.name

class Uchannel(models.Model):
    name = models.CharField(verbose_name="Uchannel Name",max_length=50)

    def __str__(self):
        return self.name

class Glass(models.Model):
    name = models.CharField(verbose_name="Glass Name",max_length=50)

    def __str__(self):
        return self.name

class Mnet(models.Model):
    name = models.CharField(verbose_name="Mosquito Net Name",max_length=50)

    def __str__(self):
        return self.name


class Quotation(models.Model):

    qid = models.CharField(verbose_name="Quotation Id", max_length=12)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    frame_type = models.CharField(verbose_name="Frame Type", max_length=30)
    frame_width = models.FloatField(verbose_name="Frame Width")
    frame_height = models.FloatField(verbose_name="Frame Height")
    frame_bar = models.FloatField(verbose_name="Frame Unit size")
    glass_rate = models.FloatField(verbose_name="Glass Rate")
    glass_type = models.CharField(verbose_name="Glass Type", max_length=30)
    glass_rate = models.FloatField(verbose_name="Glass Rate")
    il_type = models.CharField(verbose_name="I/L patti Type", max_length=30)
    il_rate = models.FloatField(verbose_name="I/L patti Rate")
    net_type = models.CharField(verbose_name="Net Type", max_length=30)
    net_rate = models.FloatField(verbose_name="Net Rate")
    uch_type = models.CharField(verbose_name="U-channel Type", max_length=30)
    uch_rate = models.FloatField(verbose_name="U-channel Rate")
    addon_type = models.CharField(verbose_name="Addon Type", max_length=30)
    addon_rate = models.FloatField(verbose_name="Addon Rate")
    
    