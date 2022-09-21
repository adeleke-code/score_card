from rest_framework import serializers
from account.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'location']


class RegisterUser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'location']

    def save(self):
        account = CustomUser(
            name=self.validated_data['name'],
            email=self.validated_data['email'],
            location=self.validated_data['location']
        )

        account.save()
        return account