from django.contrib import admin

from posts.models import Post, PostAbout


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

admin.site.register(PostAbout)
