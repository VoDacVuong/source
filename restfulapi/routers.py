from appuser.viewsets import UserViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('user', UserViewSet)