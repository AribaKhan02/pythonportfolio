from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length=255)
    applicant_name = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add=True)
    resume_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='blogimage/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
