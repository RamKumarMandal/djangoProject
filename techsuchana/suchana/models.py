from django.db import models
from django.utils.timezone import now


# Create your models here.

class TechSuchana(models.Model):
      headlines =models.CharField(max_length=500)
      author = models.CharField(max_length=50)
      created_date = models.DateTimeField(default=now, editable=False)
      teaser = models.TextField()
      largeteaser = models.TextField()
      news = models.TextField()
      image = models.ImageField(upload_to ='newspic',blank=True)
      image1 = models.ImageField(upload_to ='newspic',blank=True)
      image2 = models.ImageField(upload_to ='newspic',blank=True)
      sharelink = models.CharField(max_length=200)
      displaylink = models.CharField(max_length=50)
      home = models.BooleanField(default = False)
      latest = models.BooleanField(default=False)
      technews = models.BooleanField(default = False)
      gadgets = models.BooleanField(default = False)
      internet = models.BooleanField(default = False)
      techdeals = models.BooleanField(default = False)
      automobile = models.BooleanField(default = False)
      techsiksha = models.BooleanField(default = False)
      techjobs= models.BooleanField(default=False)
      cybercrime =models.BooleanField(default=False)

      def __str__(self):
          return self.headlines
