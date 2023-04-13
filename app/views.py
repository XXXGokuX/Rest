from rest_framework.generics import CreateAPIView
from .models import User
from .serializer import UserSerializer 
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
import bcrypt

class LoginView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = User.objects.filter(email=email).first()


        if user is None:
            return Response({'error': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)
        
        isPasswordMatch= bcrypt.checkpw(password.encode(), user.password.encode())

        if not isPasswordMatch:
            return Response({'error': 'Invalid  password'}, status=status.HTTP_401_UNAUTHORIZED)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'token': token})


class Register(CreateAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer
