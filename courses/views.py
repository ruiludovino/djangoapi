from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

# as views em django sao as webpages
# normalmente temos que criar uma funcao para cada webpage mas django nao precisa


# vamos criar paginas web, as paginas criadas 
# terao todas as linhas da BD de Course
# e sera criada um json colocado em serializer_class
class CourseView(viewsets.ModelViewSet):
	queryset= Course.objects.all() #é a nossa base de dados
	serializer_class= CourseSerializer

