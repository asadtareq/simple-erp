from django.contrib import admin
from orderappp.models import product, signuptbl

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=('name','quantity','price')
admin.site.register(product,productAdmin)

class userAdmin(admin.ModelAdmin):
    list_display=('name','email','password')
admin.site.register(signuptbl,userAdmin)