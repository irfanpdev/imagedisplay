from django.db import models
from django.core.validators import FileExtensionValidator

ext_validator=FileExtensionValidator(['png','jpg','jpeg'])
# Create your models here.
class ImageUploads(models.Model):
    imgname=models.ImageField(upload_to='img/',validators=[ext_validator])
    imgtype=models.CharField(max_length=50)

    def __str__(self):
        return self.imgtype
