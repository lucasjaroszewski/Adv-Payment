from rest_framework import serializers
from apps.users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):

    # Serializer used for Create / Update / Delete
    class Meta:
        model = Payment
        fields = ['id', 'user', 'cnpj', 'company_name', 'price', 'date_added', 'expiration_date', 'payment_status']

class PaymentEmailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    # Shows the email in the API
    # Serializer used for lists in GET requests
    def get_user(self, obj):
        return obj.user.email

    # Fields to show in the API
    class Meta:
        model = Payment
        fields = ['id', 'user', 'cnpj', 'company_name', 'price', 'date_added', 'expiration_date', 'payment_status']
