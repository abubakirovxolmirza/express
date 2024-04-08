from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Driver, Truck, Trailer, CustomerBroker, Dispatcher, Employee, Load, Stops, OtherPay, Commodities
from .serializers import DriverSerializers, TruckSerializers, TrailerSerializers, CustomerBrokerSerializers, DispatcherSerializers, EmployeeSerializers, LoadSerializers, StopsSerializers, OtherPaySerializers, CommoditiesSerializers
# Create your views here.

class DriverList(ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializers


class DriverDetail(RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializers


class TruckList(ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializers


class TruckDetail(RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializers


class TrailerList(ListCreateAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializers


class TrailerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializers


class CustomerBrokerList(ListCreateAPIView):
    queryset = CustomerBroker.objects.all()
    serializer_class = CustomerBrokerSerializers


class CustomerBrokerDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomerBroker.objects.all()
    serializer_class = CustomerBrokerSerializers


class DispatcherList(ListCreateAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializers


class DispatcherDetail(RetrieveUpdateDestroyAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializers


class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class LoadList(ListCreateAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializers


class LoadDetail(RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializers


class StopsList(ListCreateAPIView):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializers


class StopsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializers


class OtherPayList(ListCreateAPIView):
    queryset = OtherPay.objects.all()
    serializer_class = OtherPaySerializers


class OtherPayDetail(RetrieveUpdateDestroyAPIView):
    queryset = OtherPay.objects.all()
    serializer_class = OtherPaySerializers


class CommoditiesList(ListCreateAPIView):
    queryset = Commodities.objects.all()
    serializer_class = CommoditiesSerializers


class CommoditiesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Commodities.objects.all()
    serializer_class = CommoditiesSerializers

