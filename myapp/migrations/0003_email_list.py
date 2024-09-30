# Generated by Django 5.0.6 on 2024-09-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240925_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]