from django.contrib import admin

# Register your models here.
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_url', 'experience')
    search_fields = ('name', 'logo_url', 'experience')
    list_filter = ('name', 'logo_url', 'experience')
    
    
    def __str__(self):
        return self.name