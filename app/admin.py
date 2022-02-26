from django.contrib import admin

from app.models import Addon, Coat, Frame, Glass, Ilpatti, Length, Mnet, Product, Shutter, Uchannel

# Register your models here.

admin.site.register(Frame)
admin.site.register(Length)
admin.site.register(Coat)
admin.site.register(Shutter)
admin.site.register(Ilpatti)
admin.site.register(Uchannel)
admin.site.register(Glass)
admin.site.register(Mnet)

@admin.register(Addon)
class AddonAdmin(admin.ModelAdmin):
    list_display = ('product', 'item', 'nos','rate')
    list_filter = ('product',)


@admin.register(Product)
class AddonAdmin(admin.ModelAdmin):
    list_display = ('code','name')
