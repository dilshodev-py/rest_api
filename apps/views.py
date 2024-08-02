from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter , OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.filters import CategoryFilterSet
from apps.models import Category
from apps.serializers import UserSerializer, CategorySerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get']
    filter_backends = (OrderingFilter, DjangoFilterBackend, SearchFilter)
    ordering_fields = ('id', 'username')
    search_fields = ('username', 'email')
    filterset_fields = ('username', 'id')

    @action(detail=False, methods=['GET'])
    def get_me(self, requests, pk=None):
        if requests.user.is_authenticated:
            return Response({'message': f"{requests.user.username}"})
        return Response({'message': "Login qilinmagan !"})


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = DjangoFilterBackend, OrderingFilter
    filterset_class= CategoryFilterSet
    ordering_fields = 'id', 'name'

