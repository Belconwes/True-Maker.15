from django.contrib import admin
from .models import User
# Register your models here.
class usuarios(admin.ModelAdmin):
    list_display = ['email','nombre','apellido','is_admin']
    list_filter = ['id','apellido']
    search_fields = ['apellido']

admin.site.register(User,usuarios)

