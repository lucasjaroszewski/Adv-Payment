from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):

        # Serializes the data
        serializer = UserSerializer(data=request.data)

        # Validates the serializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        # Finds the user
        user = User.objects.filter(email=email).first()

        # Validate the user
        if user is None:
            raise AuthenticationFailed('User not found.')

        # Compare the password and validate
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.')

        # Stores the data the user will use with an expiration date of 60 minutes
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        # Creates the token with payload and secret
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        # Return token via cookies
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response
