from rest_framework import serializers
from .models import User
import bcrypt

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password= validated_data.pop("password")
        salt= bcrypt.gensalt()
        hashed_password= bcrypt.hashpw(password.encode(),salt)

        user= User.objects.create(password= hashed_password.decode(),**validated_data)

        return user



    class Meta:
        model= User
        fields= '__all__'
