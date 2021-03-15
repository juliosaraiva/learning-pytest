from django.urls import path, include
from rest_framework import routers
from core.views import CompanyViewSet


app_name = 'core'

router = routers.DefaultRouter()

router.register('', CompanyViewSet, basename='companies')

urlpatterns = [
    path('', include(router.urls)),
]