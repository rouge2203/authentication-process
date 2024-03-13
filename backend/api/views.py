from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserProfileSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from django.http import JsonResponse, HttpResponse


# Admin and User Login ----------------------------

class AdminLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(AdminLoginSerializer, self).validate(attrs)
        serializer = UserProfileSerializer(self.user).data

        for k, v in serializer.items():
            data[k] = v
        
        if self.user.is_staff:
            return data # User is staff and active
        
        raise PermissionDenied(detail="Permission denied, user is not a staff memeber", code=403) # User is not staff and is active

        # default: if user is not active or unvalid credentials:
            # detail="No active account found with the given credentials" code=401
    
class AdminLoginView(TokenObtainPairView):
    serializer_class = AdminLoginSerializer

class UserLoginSerializer(TokenObtainPairSerializer):                                        
    def validate(self, attrs):
        data = super(UserLoginSerializer, self).validate(attrs)
        serializer = UserProfileSerializer(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data # User is active
    
        # default: if user is not active or unvalid credentials:
            # detail="No active account found with the given credentials" code=401
    
class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


# Admin Create Staff and Users --------------------

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def AdminCreateUserView(request): # Create any account for Superusers
    if request.method == 'POST':

        if request.user.is_superuser:
            return JsonResponse({'detail':'User created successfully'}, status=201)
        
        return JsonResponse({'detail':'Permission denied, user is not a superuser'}, status=403)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def StaffCreateUserView(request): # Create users account for Staff
    if request.method == 'POST':        
        return JsonResponse({'detail':'User created successfully'}, status=201)

