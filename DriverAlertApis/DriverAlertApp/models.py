from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Routes(models.Model):

    RouteName = models.CharField(max_length=200)
    NewNews = models.TextField(max_length=1000,blank=True,null=True)
    RouteDescription = models.TextField(max_length=10000,blank=True,null=True)
    EventLatitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    EventLongitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    LatitudeArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    LongitudeArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)

    LatitudeDeltaArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    LongitudeDeltaArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)

    RouteImage = models.ImageField(upload_to='media/RoutesImage/',blank=True,null=True)
    NewsDate = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
    	verbose_name_plural = "Routes"

    def __str__(self):
    	return self.RouteName





class NewsEvent(models.Model):

    NewsName = models.CharField(max_length=200)
    NewNews = models.TextField(max_length=1000,blank=True,null=True)
    NewsDescription = models.TextField(max_length=10000,blank=True,null=True)
    EventLatitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    EventLongitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    LatitudeArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    LongitudeArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)

    LatitudeDeltaArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)
    LongitudeDeltaArea = models.DecimalField(max_digits=8, decimal_places=5, blank=True,null=True)

    NewsImage = models.ImageField(upload_to='media/NewsEEventImage/',blank=True,null=True)
    NewsDate = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
    	verbose_name_plural = "NewsEvent"

    def __str__(self):
    	return self.NewsName


