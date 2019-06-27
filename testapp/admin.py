from django.contrib import admin
from django.contrib.auth.models import Group
from testapp.models import Laptop
# from import_export.admin import I

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('lap_type','price','status','issues')
    list_per_page = 2
    list_filter = ('lap_type','issues','status')


admin.site.register(Laptop,LaptopAdmin)
# admin.site.unregister(Group)