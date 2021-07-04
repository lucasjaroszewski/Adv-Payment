from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'username']

        # Argument to not return the password
        extra_kwargs = {
            'password': {'write_only': True}
        }


    # Function to hash the password
    def create(self, validated_data):

        # Extract password
        password = validated_data.pop('password', None)

        # Creates the user instance
        instance = self.Meta.model(**validated_data)

        # Hash the password
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
