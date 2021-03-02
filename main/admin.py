from django.contrib import admin

from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]


admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created')
    list_filter = ( 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
