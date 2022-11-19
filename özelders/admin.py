from django.contrib import admin
from .models import *
""" class DersAdmin(admin.ModelAdmin):
    list_display = ['öğretmen', 'öğrenci'] """
# Register your models here.


admin.site.register(Öğrenci)
admin.site.register(Öğretmen)
admin.site.register(ÖzelDers)
admin.site.register(Ucretler)
