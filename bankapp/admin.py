from django.contrib import admin
from bankapp.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AccountAdminModel(ImportExportModelAdmin):
    list_editable = ['account_status', 'account_balance'] 
    list_display = ['user', 'account_number' ,'account_status', 'account_balance'] 
    list_filter = ['account_status']

class UserInfoAdmin(ImportExportModelAdmin):
    search_fields = ["full_name"]
    list_display = ['user', 'full_name', 'gender', 'identity_type', 'date_of_birth'] 

class TransactAdmin(ImportExportModelAdmin):
    list_display = ['sender', 'receiver', 'amount', 'description', 'timestamp']

admin.site.register(Account, AccountAdminModel)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Transaction, TransactAdmin)

