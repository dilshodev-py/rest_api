from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.models import Category


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['owner'] = UserSerializer(instance.owner).data
        return repr