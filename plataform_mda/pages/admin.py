from django.contrib import admin

from pages.models import Leader, NewUser
# Register your models here.

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):

    list_display = ('pk', 'leader_email', 'leader_name', 'leader_lastname', 'cost_center', 'product')
    list_editable = ('leader_name','product')

@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):

    list_display = ('employee_name', 'employee_lastname', 'management_consulting', 'employee_dni', 'profile_equal', 'employee_replace')
    list_editable = ('profile_equal','employee_replace')