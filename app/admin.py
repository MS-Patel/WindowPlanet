from django.contrib import admin

from app.models import Addon, Coat, Quotation, QuotationItem, Frame, Glass, Ilpatti, Length, Location, Mnet, Product, Shutter, Uchannel

# Register your models here.

admin.site.register(Frame)
admin.site.register(Length)
admin.site.register(Location)
admin.site.register(Coat)
admin.site.register(Shutter)
admin.site.register(Ilpatti)
admin.site.register(Uchannel)
admin.site.register(Glass)
admin.site.register(Mnet)
admin.site.register(Quotation)
admin.site.register(QuotationItem)

@admin.register(Addon)
class AddonAdmin(admin.ModelAdmin):
    list_display = ('item','rate')
    list_filter = ('item',)


@admin.register(Product)
class AddonAdmin(admin.ModelAdmin):
    list_display = ('code','name')



