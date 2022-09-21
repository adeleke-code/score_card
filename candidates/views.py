from django.shortcuts import render
from .serializers import CandidateSerializer
from .models import Candidates
from rest_framework import viewsets
# Create your views here.



class CandidateView(viewsets.ModelViewSet):
    queryset = Candidates.objects.all()
    serializer_class = CandidateSerializer

