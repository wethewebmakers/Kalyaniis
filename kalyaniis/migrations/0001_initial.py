# Generated by Django 3.2.9 on 2022-01-02 15:16

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('silksarees', 'Silk Saree'), ('designersarees', 'Designer Saree'), ('kurtis', 'Kurti'), ('lehenga', 'Lehenga')], default='silksarees', max_length=25)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='static/images_uploaded')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='static/images_uploaded')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='static/images_uploaded')),
                ('video', models.FileField(blank=True, null=True, upload_to='static/videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
