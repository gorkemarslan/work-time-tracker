from django.urls import path, include
from rest_framework.routers import DefaultRouter
from work_api.views import LabelViewSet, WorkViewSet

# Create a router and register our viewsets with it.
work_router = DefaultRouter()
work_router.register(r'works', WorkViewSet)
work_router.register(r'labels', LabelViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(work_router.urls)),
]
