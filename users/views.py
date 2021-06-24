from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User

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

        return Response({"message": "success"})
