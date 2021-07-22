from django.contrib import admin

from .models import GuestPost, GuestComment


admin.site.register(GuestPost)

admin.site.register(GuestComment)
