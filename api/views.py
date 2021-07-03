from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.models import User, Payment
from api.serializers import PaymentSerializer, PaymentEmailSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create':'/payment-create/',
        'Read':'/payment-list/',
        'Update':'/payment-update/<str:id>/',
        'Delete':'/payment-delete/<str:id>/',
        'Detail':'/payment-detail/<str:id>/',
    }
    return Response(api_urls)


# Endpoint for listing all payments
@api_view(['GET'])
def paymentList(request):
    payments = Payment.objects.all()
    serializer = PaymentEmailSerializer(payments, many=True)
    return Response(serializer.data)


# Endpoint for updating a Payment
@api_view(['POST', 'GET'])
def paymentUpdate(request, id):
    payment = Payment.objects.get(id=id)
    serializer = PaymentSerializer(instance=payment, data=request.data, partial=True)

    # Request validation
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# Endpoint for creating a Payment
@api_view(['POST'])
def paymentCreate(request):
    serializer = PaymentSerializer(data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()

        # Validation HTTP 201 - Created successfully
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Validation HTTP 400 - Bad request
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint for deleting a Payment
@api_view(['DELETE'])
def paymentDelete(request, id):
    payment = Payment.objects.get(id=id)
    payment.delete()

    return Response('Payment deleted successfully.')
