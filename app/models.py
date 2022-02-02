from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(verbose_name="Product Name",max_length=30)
    

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
    
    