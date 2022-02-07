from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

CATEGORY_CHOICES = (
    ('silksarees','Silk Saree'),
    ('designersarees', 'Designer Saree'),
    ('kurtis','Kurti'),
    ('lehenga','Lehenga'),
)

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='silksarees')
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1000, default='No description provided')
    image1 = models.ImageField(upload_to='static/images_uploaded', blank=False)
    image2 = models.ImageField(upload_to='static/images_uploaded',null=True, blank=True)
    image3 = models.ImageField(upload_to='static/images_uploaded',null=True, blank=True)
    image4 = models.ImageField(upload_to='static/images_uploaded',null=True, blank=True)
    image5 = models.ImageField(upload_to='static/images_uploaded',null=True, blank=True)
    video = models.FileField(upload_to='static/videos_uploaded',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], blank=True)
    date_uploaded = models.DateTimeField(default=timezone.now)