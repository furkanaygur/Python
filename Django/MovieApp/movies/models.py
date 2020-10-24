from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255, verbose_name="NAME")
    description = models.TextField(verbose_name="DESCRIPTION")
    image = models.CharField(max_length=255, verbose_name="IMAGE URL")
    created_date = models.DateTimeField(auto_now_add=True )
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        infos = str(self.name) +" "+ str(self.created_date)
        return infos

    def get_image_url(self):
        return 'img/'+self.image