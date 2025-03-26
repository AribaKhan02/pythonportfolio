from django.contrib import admin
from .models import Certificate, Resume, ContactMessage, BlogPost
from  ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget': CKEditorUploadingWidget()}
    }

admin.site.register(Certificate)
admin.site.register(Resume)
admin.site.register(ContactMessage)
admin.site.register(BlogPost,BlogPostAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

