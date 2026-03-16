from django.contrib import admin
from .models import GyanChakraUserModel
# Register your models here.

class GyanChakraUserModelAdmin(admin.ModelAdmin):
    list_display = ('email','name','profession', 'phone', 'address','facebook_id_link','admin_approval','is_active')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('phone', 'email')

admin.site.register(GyanChakraUserModel, GyanChakraUserModelAdmin)