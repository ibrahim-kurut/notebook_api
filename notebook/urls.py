from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotebookViewSet

router = DefaultRouter()
router.register(r'note', NotebookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]