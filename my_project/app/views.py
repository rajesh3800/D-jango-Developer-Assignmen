from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer


def home(request):
    return render(request, 'home.html')

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            vendor = serializer.validated_data['vendor']
            serializer.save()
            # Calculate and update performance metrics
            self.update_performance_metrics(vendor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_performance_metrics(self, vendor):
        # Calculate metrics and update Vendor model
        # Logic for updating historical performance may also be implemented here
        pass

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        # Calculate and update performance metrics
        self.update_performance_metrics(instance.vendor)

    def perform_destroy(self, instance):
        vendor = instance.vendor
        instance.delete()
        # Calculate and update performance metrics
        self.update_performance_metrics(vendor)

    def update_performance_metrics(self, vendor):
        # Calculate metrics and update Vendor model
        # Logic for updating historical performance may also be implemented here
        pass
