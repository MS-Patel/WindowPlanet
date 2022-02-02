from django.contrib import admin

from app.models import Coat, Frame, Glass, Ilpatti, Length, Mnet, Product, Quotation, Shutter, Uchannel

# Register your models here.

admin.site.register(Product)
admin.site.register(Frame)
admin.site.register(Length)
admin.site.register(Coat)
admin.site.register(Shutter)
admin.site.register(Ilpatti)
admin.site.register(Uchannel)
admin.site.register(Glass)
admin.site.register(Mnet)
admin.site.register(Quotation)