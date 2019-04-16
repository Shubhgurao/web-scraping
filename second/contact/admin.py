from django.contrib import admin
from .models import contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    



    admin.site.register(contact)