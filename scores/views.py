from django.shortcuts import render
from .serializers import ScoreSerializer
from .models import Scores
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.



class ScoreView(APIView):
    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully saved candidates scores.'
            data['id'] = account.id
            data['email'] = account.user_id
            data['user_id'] = account.candidates_id
        else:
            data = serializer.errors

        return Response(data)