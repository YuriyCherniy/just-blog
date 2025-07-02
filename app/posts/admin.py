from django.contrib import admin

from wysiwyg_img.admin import ImageInline

from posts.models import PostImage, Post, PostAbout


class PostImageInline(ImageInline):
    model = PostImage

class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
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
