from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("employees",views.EmployeeViewsetView,basename="employees"),

urlpatterns=[

]+router.urls