from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializers


class UserModelAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)
