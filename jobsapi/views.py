from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import JobSerializer
from .models import Jobs
from rest_framework import permissions

# Create your views here.
class Joblist(ListCreateAPIView):

    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user)

    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user)  


class JobDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user)          