from django.db import models

class Movie(models.Model):
    # define a username filed with bound  max length it can have
    title = models.CharField(max_length=200)

    # This is used to get the video
    video = models.FileField(upload_to='videos/', null=True, verbose_name="")   
    
    def __str__(self):
        return self.title + ": " + str(self.video)