from django.contrib import admin
from .models import Certificate, Resume, ContactMessage

admin.site.register(Certificate)
admin.site.register(Resume)
admin.site.register(ContactMessage)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')