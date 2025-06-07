from django.contrib import admin
from Beats.models import Beat
# Register your models here.
class BeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Beat, BeatAdmin)