
from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('Routes', views.RoutesViewSet)
router.register('News', views.NewsEventViewSet)



urlpatterns = router.urls