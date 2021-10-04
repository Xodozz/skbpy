from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.site_url = 'http://127.0.0.1:8000/blog'

admin.site.register(Post, PostAdmin)
