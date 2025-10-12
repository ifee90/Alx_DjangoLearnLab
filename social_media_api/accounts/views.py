from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes

from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer


# -----------------------------
# 1️⃣ User Registration View
# -----------------------------
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Open registration

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": serializer.data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


# -----------------------------
# 2️⃣ User Login View
# -----------------------------
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            "message": "Login successful",
            "token": token.key
        }, status=status.HTTP_200_OK)


# -----------------------------
# 3️⃣ Follow a User
# -----------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    if target_user == request.user:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    if target_user in request.user.following.all():
        return Response({"message": f"You already follow {target_user.username}."}, status=status.HTTP_200_OK)

    request.user.following.add(target_user)
    return Response({"message": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)


# -----------------------------
# 4️⃣ Unfollow a User
# -----------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    if target_user == request.user:
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    if target_user not in request.user.following.all():
        return Response({"message": f"You are not following {target_user.username}."}, status=status.HTTP_200_OK)

    request.user.following.remove(target_user)
    return Response({"message": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)
