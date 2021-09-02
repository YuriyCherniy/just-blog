from django.contrib import admin

from .models import GuestPost, GuestComment


class GuestCommentInline(admin.TabularInline):
    model = GuestComment


class GuestPostAdmin(admin.ModelAdmin):
    inlines = [
        GuestCommentInline,
    ]


admin.site.register(GuestPost, GuestPostAdmin)
