from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# internal imports
from .models import GyanChakraUserModel
from .serializers import GyanChakraUserCreateSerializer

# Jwt imports
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class GyanChakraUserCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new GyanChakra user by providing necessary information.",
        request_body=GyanChakraUserCreateSerializer,
        
        responses={201: GyanChakraUserCreateSerializer}
    )
    def post(self, request):
        serializer = GyanChakraUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GyanChakraUserLoginAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Login a GyanChakra user by providing email and password.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
            },
            required=['email', 'password']
        ),
        responses={200: 'Login successful', 400: 'Invalid credentials'}
    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = GyanChakraUserModel.objects.get(email=email)
            
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except GyanChakraUserModel.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        

