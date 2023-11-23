from django.contrib import admin
from passwordDatabase.models import PasswordDatabase

class PasswordDatabaseAdmin(admin.ModelAdmin):
    list_display=('db_name','db_password','db_slug','db_user')

admin.site.register(PasswordDatabase, PasswordDatabaseAdmin)
# Register your models here.
