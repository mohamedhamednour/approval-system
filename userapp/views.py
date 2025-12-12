from rest_framework import mixins, viewsets

from .serializers import (
    LoginSerializer,
    UserSerializer,
    RefreshTokenSerializer,
    UpdateProfileSerializer,
    BaseUserSerializer,
    LougoutSerializer,
    GoogleAuthSerializer
)
from .models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        if self.action == "register":
            return UserSerializer
        if self.action == "refresh_token":
            return RefreshTokenSerializer
        if self.action == "update_profile":
            return UpdateProfileSerializer
        if self.action == "get_profile":
            return BaseUserSerializer
        if self.action == "logout":
            return LougoutSerializer
        return super().get_serializer_class()

    @action(methods=["post"], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    @action(detail=False, methods=["post"])
    def refresh_token(self,request):
        serializer = RefreshTokenSerializer(data=request.data)
        if serializer.is_valid ():
            return Response({"data": serializer.data})
        return Response({"error": serializer.errors} , status=400)
    

    @action(detail=False, methods=["patch"], url_path="update-profile", permission_classes=[IsAuthenticated])
    def update_profile(self ,request):
        user = request.user
        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)
        if  serializer.is_valid ():
            serializer.save()
            return Response({"data": serializer.data})    
        return Response({"error": serializer.errors} , status=400)
    

    @action(detail=False, methods=["get"], url_path="get-profile", permission_classes=[IsAuthenticated])
    def get_profile(self ,request):
        user = request.user
        serializer = BaseUserSerializer(user)
        return Response({"data": serializer.data})
    

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request):
        serializer = LougoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh = serializer.validated_data['refresh_token']
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({"detail": "Logout successful"})
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
