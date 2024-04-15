from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import filters
from django.db import models

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Driver, Truck, Trailer, CustomerBroker, Dispatcher, Employee, Load, Stops, OtherPay, Commodities, LoadTags, EmployeeTags, DispatcherTags, TruckTags, TrailerTags, DriverTags
from .serializers import DriverSerializers, TruckSerializers, TrailerSerializers, CustomerBrokerSerializers, DispatcherSerializers, EmployeeSerializers, LoadSerializers, StopsSerializers, OtherPaySerializers, CommoditiesSerializers, LoadTagsSerializers, TruckTagsSerializers, TrailerTagsSerializers, DispatcherTagsSerializers, EmployeeTagsSerializers, DriverTagsSerializers
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['load_status', 'load_id']

    def list(self, request, *args, **kwargs):
        order = request.query_params.get('order', 'asc')

        # Filter queryset
        queryset = self.filter_queryset(self.get_queryset())

        if order == 'desc':
            queryset = queryset.order_by('-id')
        else:
            queryset = queryset.order_by('id')

        # Sums
        total_load_pay = queryset.aggregate(total_load_pay=models.Sum('load_pay'))['total_load_pay'] or 0
        total_miles_all = queryset.aggregate(
            total_miles_all=models.Sum('total_miles', output_field=models.DecimalField(max_digits=10, decimal_places=2))
        )['total_miles_all'] or 0
        total_empty_mile = queryset.aggregate(
            total_empty_mile=models.Sum('empty_mile', output_field=models.DecimalField(max_digits=10, decimal_places=2))
        )['total_empty_mile'] or 0
        total_driver_pay = queryset.aggregate(total_driver_pay=models.Sum('driver_pay'))['total_driver_pay'] or 0

        total_driver_charge = queryset.aggregate(
            total_driver_charge=models.Sum(models.ExpressionWrapper(models.F('load_pay') * models.F('driver__tariff'), output_field=models.DecimalField(max_digits=10, decimal_places=2)))
        )['total_driver_charge'] or 0

        total_driver_charge += total_driver_pay

        per_total_miles = models.DecimalField(max_digits=10, decimal_places=2)
        if total_miles_all > 0:
            per_total_miles = total_load_pay / total_miles_all
        else:
            per_total_miles = 0

        serializer = self.get_serializer(queryset, many=True)

        data = serializer.data
        for load in data:
            load['total_load_pay'] = total_load_pay
            load['total_miles_all'] = total_miles_all
            load['total_empty_miles'] = total_empty_mile
            load['total_driver_charge'] = total_driver_charge
            load['per_total_miles'] = per_total_miles

        return Response(data)


class LoadDetail(RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['load_status', 'load_id']

    def list(self, request, *args, **kwargs):
        order = request.query_params.get('order', 'asc')

        # Filter queryset
        queryset = self.filter_queryset(self.get_queryset())

        if order == 'desc':
            queryset = queryset.order_by('-id')
        else:
            queryset = queryset.order_by('id')

        # Sums
        total_load_pay = queryset.aggregate(total_load_pay=models.Sum('load_pay'))['total_load_pay'] or 0
        total_miles_all = queryset.aggregate(
            total_miles_all=models.Sum('total_miles', output_field=models.DecimalField(max_digits=10, decimal_places=2))
        )['total_miles_all'] or 0
        total_empty_mile = queryset.aggregate(
            total_empty_mile=models.Sum('empty_mile', output_field=models.DecimalField(max_digits=10, decimal_places=2))
        )['total_empty_mile'] or 0
        total_driver_pay = queryset.aggregate(total_driver_pay=models.Sum('driver_pay'))['total_driver_pay'] or 0

        total_driver_charge = queryset.aggregate(
            total_driver_charge=models.Sum(models.ExpressionWrapper(models.F('load_pay') * models.F('driver__tariff'),
                                                                    output_field=models.DecimalField(max_digits=10,
                                                                                                     decimal_places=2)))
        )['total_driver_charge'] or 0

        total_driver_charge += total_driver_pay

        if total_miles_all > 0:
            per_total_miles = total_load_pay / total_miles_all
        else:
            per_total_miles = 0

        serializer = self.get_serializer(queryset, many=True)

        data = serializer.data
        for load in data:
            load['total_load_pay'] = total_load_pay
            load['total_miles_all'] = total_miles_all
            load['total_empty_miles'] = total_empty_mile
            load['total_driver_charge'] = total_driver_charge
            load['per_total_miles'] = per_total_miles

        return Response(data)

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


class LoadTagsList(ListCreateAPIView):
    queryset = LoadTags.objects.all()
    serializer_class = LoadTagsSerializers


class LoadTagsDetail(RetrieveUpdateDestroyAPIView):
    queryset = LoadTags.objects.all()
    serializer_class = LoadTagsSerializers


class EmployeeTagsList(ListCreateAPIView):
    queryset = EmployeeTags.objects.all()
    serializer_class = EmployeeTagsSerializers


class EmployeeTagsDetail(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeTags.objects.all()
    serializer_class = EmployeeTagsSerializers


class TrailerTagsList(ListCreateAPIView):
    queryset = TrailerTags.objects.all()
    serializer_class = TrailerTagsSerializers


class TrailerTagsDetail(RetrieveUpdateDestroyAPIView):
    queryset = TrailerTags.objects.all()
    serializer_class = TrailerTagsSerializers


class TruckTagsList(ListCreateAPIView):
    queryset = TruckTags.objects.all()
    serializer_class = TruckTagsSerializers


class TruckTagsDetail(RetrieveUpdateDestroyAPIView):
    queryset = TruckTags.objects.all()
    serializer_class = TruckTagsSerializers


class DriverTagsList(ListCreateAPIView):
    queryset = DriverTags.objects.all()
    serializer_class = DriverTagsSerializers


class DriverTagsDetail(RetrieveUpdateDestroyAPIView):
    queryset = DriverTags.objects.all()
    serializer_class = DriverTagsSerializers


class DispatcherTagsList(ListCreateAPIView):
    queryset = DispatcherTags.objects.all()
    serializer_class = DispatcherTagsSerializers


class DispatcherTagsDetail(RetrieveUpdateDestroyAPIView):
    queryset = DispatcherTags.objects.all()
    serializer_class = DispatcherTagsSerializers


