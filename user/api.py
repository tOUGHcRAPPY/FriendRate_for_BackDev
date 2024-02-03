from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializers


class UserModelAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [permissions.AllowAny()]
        else:
            return super().get_permissions()
