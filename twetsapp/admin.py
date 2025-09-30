from django.contrib import admin
from .models import Twet

@admin.register(Twet)
class TwetAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_at")
    search_fields = ("user__username", "content")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
