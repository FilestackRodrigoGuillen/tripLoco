from django.db import models

class PostCardHeader(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    photo_cover = models.CharField(max_length=250, blank=True, null=True)
    photo_polaroid= models.CharField(max_length=250, blank=True, null=True)
    cover_workflow = models.CharField(max_length=250, blank=True, null=True)
    photo_flag = models.CharField(max_length=250, blank=True, null=True)
    location_link = models.CharField(max_length=250, blank=True, null=True)
    photo_weather = models.CharField(max_length=250, blank=True, null=True)
    ocr_workflow = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.photo_cover
    
