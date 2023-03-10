from django.contrib import admin
from contact.models import ContactMe

# Register your models here.
@admin.register(ContactMe)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email', 'message')

