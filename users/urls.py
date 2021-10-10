from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import EmployeeViewSet, RoleViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'roles', RoleViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
