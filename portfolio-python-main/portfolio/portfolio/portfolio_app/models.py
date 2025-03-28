from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.title

