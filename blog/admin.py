from django.contrib import admin
from .models import Post, Contact, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'admin_photo', 'created_at', 'is_published')
    search_fields = ('title', 'description')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_solved')


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
