from django.contrib import admin

from posts.models import Post, PostAbout, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = [
        'get_image_url', 'get_image_tag',
    ]


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

admin.site.register(PostAbout)
