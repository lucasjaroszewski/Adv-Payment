from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

        # Argument to not return the password
        extra_kwargs = {
            'password': {'write_only': True}
        }


    # Function to hash the password
    def create(self, validated_data):
        password = validated_data.pop('password', None)     # Extract password
        instance = self.Meta.model(**validated_data)        # Creates the user instance
        
        if password is not None:
            instance.set_password(password)                 # Hash the password

        instance.save()                                     # Saves the user instance
        return instance
