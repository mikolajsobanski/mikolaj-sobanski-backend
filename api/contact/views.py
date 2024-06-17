from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactFormSerializer

class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            send_mail(
                'New Contact Form Submission',
                f"You have a new contact form submission from {data['firstName']} {data['lastName']}.\n"
                f"Email: {data['email']}\n"
                f"Phone: {data['phone']}\n"
                f"Message: {data['message']}",
                data['email'],
                ['mikolajsobanski01@gmail.com'],  
            )
            return Response({'message': 'Message sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
