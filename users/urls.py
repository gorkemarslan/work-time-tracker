from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import EmployeeViewSet, RoleViewSet

# Create a router and register our viewsets with it.
user_router = DefaultRouter()
user_router.register(r'employees', EmployeeViewSet)
user_router.register(r'roles', RoleViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(user_router.urls)),
]
