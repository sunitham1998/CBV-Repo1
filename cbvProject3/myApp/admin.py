from django.contrib import admin
from myApp.models import HOD

# Register your models here.
class HODAdmin(admin.ModelAdmin):
     l=['name','no','exp','sal']
admin.site.register(HOD,HODAdmin)

