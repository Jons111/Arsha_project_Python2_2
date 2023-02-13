from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','nomi','company_name','date','rasm1']

admin.site.register(Portfolio,AdminPortfolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi',]

admin.site.register(Type,AdminType)


class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id','name','mail','title','text','date']

admin.site.register(Murojaat,AdminMurojaat)