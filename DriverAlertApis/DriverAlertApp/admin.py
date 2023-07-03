from django.contrib import admin
from .models import *

# Register your models here.
class RoutesAdmin(admin.ModelAdmin):

	list_display = ["RouteName", "NewsDate","LatitudeArea","LongitudeArea","EventLatitude","EventLongitude"]
	list_filter =["NewsDate","Updated"]
	search_fields = ["RouteName"]


class NewsEventAdmin(admin.ModelAdmin):

	list_display = ["NewsName", "NewsDate","LatitudeArea","LongitudeArea","EventLatitude","EventLongitude"]
	list_filter =["NewsDate","Updated"]
	search_fields = ["NewsName"]



admin.site.register(Routes, RoutesAdmin)
admin.site.register(NewsEvent, NewsEventAdmin)