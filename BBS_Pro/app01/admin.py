from django.contrib import admin
from app01 import models

# Register your models here.


class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'auth')


admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
