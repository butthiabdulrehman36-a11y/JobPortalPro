from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company_name",
        "location",
        "employment_type",
        "is_active",
        "created_at",
    )
    list_filter = (
        "employment_type",
        "is_active",
        "created_at",
    )
    search_fields = (
        "title",
        "company_name",
        "location",
        "description",
    )
    ordering = ("-created_at",)
