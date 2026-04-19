from rest_framework import generics, status, permissions
from .serializers import RegisterSerializer, LoginSerializer
from .models import User

# Create your views here.


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    
class LoginView(generics.)    
    
