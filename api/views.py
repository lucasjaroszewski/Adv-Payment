from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.models import User, Payment
from apps.core.tasks import send_email_status
from api.serializers import PaymentSerializer, PaymentEmailSerializer
import json, logging

# Logging Configuration
logging.basicConfig(filename='Adv-Payment.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Payments':'------------------------',
        'Create':'/payment-create/',
        'Read':'/payment-list/',
        'Update':'/payment-update/<str:id>/',
        'Delete':'/payment-delete/<str:id>/',
        'Detail':'/payment-detail/<str:id>/',
        'Users':'---------------------------',
        'User':'/user/',
        'Register':'/register/',
        'Login':'/login/',
        'Logout':'/logout/',
    }
    return Response(api_urls)


# Endpoint for listing all payments
@api_view(['GET'])
def paymentList(request):
    payments = Payment.objects.all()
    serializer = PaymentEmailSerializer(payments, many=True)
    return Response(serializer.data)


# Endpoint for updating a Payment
@api_view(['GET', 'POST'])
def paymentUpdate(request, id):

    payment = Payment.objects.get(id=id)
    serializer = PaymentSerializer(instance=payment, data=request.data, partial=True)

    # Gets data from request
    dump = json.dumps(request.data)
    data = json.loads(dump)

    # Identifies e-mail and payment status change
    payment_status = data['payment_status']
    email = data['email']
    payment_id = payment.id

    # Request validation
    if serializer.is_valid():
        serializer.save()
        logging.info('Payment #{} status changed to: {}.'.format(payment_id, payment_status))

        # Send e-mail to user throught Celery Task
        send_email_status(payment_status, email)
        logging.info('E-mail sent to: {}.'.format(email))

        # Validation HTTP 201 - Created successfully
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Validation HTTP 400 - Bad request
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint for creating a Payment
@api_view(['POST'])
def paymentCreate(request):

    # Gets data from request
    dump = json.dumps(request.data)
    data = json.loads(dump)

    # Identifies e-mail and payment status change
    payment_status = data['payment_status']
    email = data['email']

    # Serializer the data
    serializer = PaymentSerializer(data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()
        logging.info('A new Payment was created')

        # Send e-mail to user throught Celery Task
        send_email_status(payment_status, email)
        logging.info('E-mail sent to: {}.'.format(email))

        # Validation HTTP 201 - Created successfully
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Validation HTTP 400 - Bad request
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint for deleting a Payment
@api_view(['DELETE'])
def paymentDelete(request, id):
    payment = Payment.objects.get(id=id)
    payment_id = payment.id

    payment.delete()
    logging.warning('Payment #{} was deleted.'.format(payment_id))

    return Response('Payment deleted successfully.')
