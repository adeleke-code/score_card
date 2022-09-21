from django.urls import path, include
from rest_framework import routers
from .views import CandidateView



router = routers.DefaultRouter()
router.register(r'candidates', CandidateView)


urlpatterns = [
    path('', include(router.urls))
]

