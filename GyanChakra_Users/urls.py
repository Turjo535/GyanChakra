from django.urls import path
# Authviews imports
from .views import GyanChakraUserCreateAPIView, GyanChakraUserLoginAPIView
urlpatterns = [
    path('create-user/', GyanChakraUserCreateAPIView.as_view(), name='user-create'),
    path('login/', GyanChakraUserLoginAPIView.as_view(), name='user-login'),
]