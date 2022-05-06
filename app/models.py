from django.db import models

class Product(models.Model):
    code = models.CharField(verbose_name="Product Code", max_length=10, unique=True)
    name = models.CharField(verbose_name="Product Name", max_length=50)
    image = models.CharField(max_length=255,blank=True,null=True)
    discription=models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Frame(models.Model):
    name = models.CharField(verbose_name="Frame Name", max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(verbose_name="Location", max_length=50)

    def __str__(self):
        return self.name

class Length(models.Model):
    name = models.CharField(verbose_name="Length", max_length=50)

    def __str__(self):
        return self.name


class Coat(models.Model):
    name = models.CharField(verbose_name="Coating Name", max_length=50)
    rate = models.FloatField(verbose_name="Rate")

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

    item = models.CharField(verbose_name="Item Name", max_length=50)
    rate = models.FloatField(verbose_name="Rate")

    def __str__(self):
        return self.item
    
class Quotation(models.Model):
     id = models.CharField(max_length=10,primary_key=True)
     total_qty = models.DecimalField(verbose_name="Total Qty", max_digits=5, decimal_places=0)
     totalvalue=models.FloatField(verbose_name="Total Value")
     totalsize=models.FloatField(verbose_name="Total Size")
     totallabour=models.FloatField(verbose_name="Total labour")
     total_transport_charge=models.FloatField(verbose_name="Total Transport Charge")
     finalvalue=models.FloatField(verbose_name="Final Value")
     gst=models.FloatField(verbose_name="GST")
     summery=models.FloatField(verbose_name="Grand Total")
     quotation_date= models.DateField(auto_now_add=False)
     to = models.CharField(verbose_name="To", max_length=50)
     to_address_line_1 = models.CharField(verbose_name="To Address Line 1", max_length=20)
     to_address_line_2 = models.CharField(verbose_name="To Address Line 2", max_length=20)
     to_address_line_3 = models.CharField(verbose_name="To Address Line 3", max_length=20)
     to_contact_no = models.DecimalField(verbose_name="To Contact No", max_digits=12 , decimal_places=0)
     deliver_to = models.CharField(verbose_name="Deliver To", max_length=50)
     deliver_to_address_line_1  = models.CharField(verbose_name="Deliver To Address Line 1", max_length=20)
     deliver_to_address_line_2  = models.CharField(verbose_name="Deliver To Address Line 2", max_length=20)
     deliver_to_address_line_3  = models.CharField(verbose_name="Deliver To Address Line 3", max_length=20)
     deliver_to_contact_no  = models.DecimalField(verbose_name="Deliver To Contact No", max_digits=12 , decimal_places=0)
     customer_reference = models.CharField(verbose_name="Customer Reference", max_length=50)
     responsible = models.CharField(verbose_name="Responsible", max_length=50)
     

     def __str__(self):
         return self.id
         
class QuotationItem(models.Model):
     qoutation = models.ForeignKey(Quotation,on_delete=models.PROTECT)
     product=models.ForeignKey(Product,on_delete=models.PROTECT,related_name="dispaly")
     section = models.CharField(max_length=50, null=True)
     h = models.FloatField(verbose_name="item height")
     w = models.FloatField(verbose_name="item weight")
     size = models.FloatField(verbose_name="item size")
     location = models.CharField(max_length=25, verbose_name="Location")
     shutter = models.CharField(max_length=50, null=True)
     glass = models.CharField(max_length=50, null=True)
     unitprice=models.FloatField(verbose_name="Total")
     qty=models.DecimalField(verbose_name="Qty", max_digits=5, decimal_places=0)
     value=models.FloatField(verbose_name="Value")
     labour=models.FloatField(verbose_name="Labour")
     transport_charge=models.FloatField(verbose_name="Transport Charge")
     pl = models.CharField(max_length=50, null=True)
     hl = models.CharField(max_length=50, null=True)
     def __str__(self):
         return self.qoutation.id

