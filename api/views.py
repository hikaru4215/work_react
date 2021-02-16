from django.shortcuts import render
from rest_framework import generics
from api.models import Profile
from api.permissions import IsAdminUserOrReadOnly
from api.serializers import ProfileSerializer


class ListView(generics.ListAPIView):
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class DetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUserOrReadOnly]