from django.contrib import admin
from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email', 'message')

