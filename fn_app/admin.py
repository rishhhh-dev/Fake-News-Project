from django.contrib import admin
from fn_app.models import post
# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','date_posted','author']


admin.site.register(post,TitleAdmin)
