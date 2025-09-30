from django.contrib import admin
from .models import Twet

@admin.register(Twet)
class TwetAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_at")
    search_fields = ("user__username", "content")
