from email.mime import image
from rest_framework import serializers
from .models import Candidates



class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = '__all__'


   
        