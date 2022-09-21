from django.shortcuts import render
from account.serializers import RegisterUser
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterUser(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new user.'
            data['email'] = account.email
            data['user_id'] = account.id
        else:
            data = serializer.errors

        return Response(data)