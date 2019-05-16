from django.contrib import admin
from .models import Area, AreaCode, Schedule

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    class Meta: 
        model = Area

class AreaCodeAdmin(admin.ModelAdmin):
    class Meta:
        model = AreaCode

class ScheduleAdmin(admin.ModelAdmin):
    class Meta:
        model = Schedule

admin.site.register(Area)
admin.site.register(AreaCode)
admin.site.register(Schedule)