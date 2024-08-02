from django.urls import path

from apps.views import  CategoryListCreateAPIView



urlpatterns = [
    path('categories', CategoryListCreateAPIView.as_view(), name='category'),
]