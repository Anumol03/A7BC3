# Generated by Django 5.0.6 on 2024-09-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_email_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_list',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
