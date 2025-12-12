from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet , CompanyViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('companies', CompanyViewSet)



urlpatterns = [
    path('', include(router.urls)),
]