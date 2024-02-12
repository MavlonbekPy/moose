from django.contrib import admin
from .models import Post, Contact, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'admin_photo', 'created_at', 'is_published')
    search_fields = ('title', 'description')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_solved')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
