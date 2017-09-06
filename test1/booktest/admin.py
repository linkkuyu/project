from django.contrib import admin

# Register your models here.
from .models import *

class HeroInfoInline(admin.StackedInline):#TarbularInline表格的样式
    model = HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']
    list_filter = ['btitle']
    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInfoAdmin)