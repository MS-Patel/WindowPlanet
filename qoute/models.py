from django.db import models

from app.models import Addon, Coat, Frame, Glass, Ilpatti, Length, Location, Mnet, Product, Uchannel


class Products(models.Model):

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    frame_type = models.ForeignKey(
        Frame, on_delete=models.PROTECT, max_length=30)
    frame_width = models.FloatField(verbose_name="Frame Width")
    frame_height = models.FloatField(verbose_name="Frame Height")
    frame_bar = models.ForeignKey(
        Length, on_delete=models.PROTECT, verbose_name="Frame Unit size")
    frame_rate = models.FloatField(verbose_name="Frame Rate")
    glass_type = models.ForeignKey(
        Glass, on_delete=models.PROTECT, verbose_name="Glass Type", max_length=30)
    glass_rate = models.FloatField(verbose_name="Glass Rate")
    il_type = models.ForeignKey(
        Ilpatti, on_delete=models.PROTECT, verbose_name="I/L patti Type", max_length=30)
    il_rate = models.FloatField(verbose_name="I/L patti Rate")
    net_type = models.ForeignKey(
        Mnet, on_delete=models.PROTECT, verbose_name="Net Type", max_length=30)
    net_rate = models.FloatField(verbose_name="Net Rate")
    uch_type = models.ForeignKey(
        Uchannel, on_delete=models.PROTECT, verbose_name="U-channel Type", max_length=30)
    uch_rate = models.FloatField(verbose_name="U-channel Rate")
    coat_type = models.ForeignKey(
        Coat, on_delete=models.PROTECT, verbose_name="Coating Type", max_length=30)
    coat_rate = models.FloatField(verbose_name="Coating Rate")
    qty= models.PositiveIntegerField(verbose_name="Quantity")
    location=models.ForeignKey(
        Location, on_delete=models.PROTECT, max_length=30)

class Quotation(models.Model):

    _id = models.IntegerField(verbose_name="Quotation Id", auto_created=True)
    items = models.ManyToManyField(Products,verbose_name="items")
    addon_type = models.ManyToManyField(
        Addon, verbose_name="Addon Type", max_length=30)
    addon_rate = models.FloatField(verbose_name="Addon Rate")
