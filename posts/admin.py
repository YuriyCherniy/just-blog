from django.contrib import admin

from posts.models import Post, PostAbout


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = [
        'get_image_url', 'get_image_url_1',
        'get_image_url_2', 'get_image_url_3',
        'get_image_url_4', 'get_image_url_5',
        'get_image_url_6', 'get_image_url_7',
        'get_image_url_8', 'get_image_url_9',
        'get_image', 'get_image_1',
        'get_image_2', 'get_image_3',
        'get_image_4', 'get_image_5',
        'get_image_6', 'get_image_7',
        'get_image_8', 'get_image_9'
    ]
    empty_value_display = '- изображение не загруженно -'

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'poster', 'text')
        }),
        ('Изображение 1', {
            'fields': ('image', 'get_image_url', 'get_image')
        }),
        ('Изображение 2', {
            'fields': ('image_1', 'get_image_url_1', 'get_image_1')
        }),
        ('Изображение 3', {
            'fields': ('image_2', 'get_image_url_2', 'get_image_2')
        }),
        ('Изображение 4', {
            'fields': ('image_3', 'get_image_url_3', 'get_image_3')
        }),
        ('Изображение 5', {
            'fields': ('image_4', 'get_image_url_4', 'get_image_4')
        }),
        ('Изображение 6', {
            'fields': ('image_5', 'get_image_url_5', 'get_image_5')
        }),
        ('Изображение 7', {
            'fields': ('image_6', 'get_image_url_6', 'get_image_6')
        }),
        ('Изображение 8', {
            'fields': ('image_7', 'get_image_url_7', 'get_image_7')
        }),
        ('Изображение 9', {
            'fields': ('image_8', 'get_image_url_8', 'get_image_8')
        }),
        ('Изображение 10', {
            'fields': ('image_9', 'get_image_url_9', 'get_image_9')
        }),
        ('Теги поста', {
            'fields': ('tag',)
        }),

    )


admin.site.register(Post, PostAdmin)

admin.site.register(PostAbout)
