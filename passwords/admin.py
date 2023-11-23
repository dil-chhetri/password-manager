from django.contrib import admin
from passwords.models import Password

class PasswordAdmin(admin.ModelAdmin):
    list_display=('username','password','url','password_db')

admin.site.register(Password, PasswordAdmin)

# Register your models here.
