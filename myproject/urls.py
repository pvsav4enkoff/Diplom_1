"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from plant.views import *

urlpatterns = [
    path('', view_plant), 
    path('admin/', admin.site.urls),
    path('plant/', view_plant),
    path('plant/employee/edit/<pk>/', edit_employee, name='edit_employee'),
    path('plant/repair', view_plant_repair,name='repairs_list'),
    path('plant/task', view_plant_task,name='task_list'),
    path('plant/equipment', view_plant_equipment),
    path('plant/employee', view_plant_employee, name='employee_main'),
    path('plant/employee/sign_up', sign_up_by_plant),
    path('plant/equipment/sign_equipment', registration_equipment),
    path('plant/equipment/sign_repair', registration_repair),
    path('plant/employee/sign_task', registration_task),
    path('repair/complete_repair/<pk>/', complete_repair, name='complete_repair'),
    path('task/complete_task/<pk>/', complete_task, name='complete_task'),
    path('plant/task', sort_view, name='sort_view'),
    path('export_to_excel_task/', export_to_excel_task, name='export_to_excel_task'),


]
