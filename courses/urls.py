# para correr o admin do Django:
# no terminal : 
# python manage.py startapp courses

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# courses vai ser o url
router.register('courses', views.CourseView)

urlpatterns = [
	path('', include(router.urls)),    
]
