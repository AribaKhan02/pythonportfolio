# Generated by Django 5.1.7 on 2025-03-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('issuer', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to='certificates/')),
            ],
        ),
    ]
