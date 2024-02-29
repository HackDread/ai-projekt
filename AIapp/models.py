from django.db import models

# Create your models here.


class Imageai(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    Image_ai = models.ImageField(upload_to="mediaai", blank=True, null=True)

    def __str__(self):
        return self.title
    
class Meta:
    varbose_name = "Imageai"
    varbose_name_piural = "ObrazyAi"