from django.contrib import admin
from .models import user_create
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.

class user_create_admin(admin.ModelAdmin):
    list_display = ('username','is_active' ,'date_joined','email')
    list_filter = (('date_joined', DateRangeFilter), ('date_joined', DateTimeRangeFilter))  
    list_editable = ('is_active',)
    change_list_template  = 'admin/user_change_list.html'

admin.site.register(user_create, user_create_admin)
