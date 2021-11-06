from django.contrib import admin
from .models import Post, Banner

from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'slug', 'status', 'created_on','image_img')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    readonly_fields = ["preview"]
    prepopulated_fields = {'slug': ('title',),}

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

class BannerAdmin(admin.ModelAdmin):

    list_display = ('image_img',)


admin.site.site_url = 'http://127.0.0.1:8000/blog'

admin.site.register(Post,PostAdmin)
admin.site.register(Banner,BannerAdmin)
