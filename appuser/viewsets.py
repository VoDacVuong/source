from rest_framework import viewsets
from . import models
from . import serializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.user.objects.all()
    serializer_class = serializer.UserSerializer