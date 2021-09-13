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
    fields = (
        'title', 'slug', 'description_tag',
        'poster', 'text', 'is_published', 'tag'
    )


class PostAboutAdmin(admin.ModelAdmin):
    fields = ('title', 'description_tag', 'text')


admin.site.register(Post, PostAdmin)

admin.site.register(PostAbout, PostAboutAdmin)
