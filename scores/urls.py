from django.urls import path, include
from .views import ScoreView




urlpatterns = [
    path('', ScoreView.as_view()),
]

