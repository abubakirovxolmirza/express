from rest_framework import serializers
from .models import Driver, Truck, Trailer, CustomerBroker, Dispatcher, Employee, Load, Stops, OtherPay, Commodities, LoadTags, EmployeeTags, DispatcherTags, TruckTags, TrailerTags, DriverTags


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class TruckSerializers(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"


class TrailerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = "__all__"


class CustomerBrokerSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerBroker
        fields = "__all__"


class DispatcherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dispatcher
        fields = "__all__"


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class LoadSerializers(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.nickname')
    customer_broker = serializers.ReadOnlyField(source='customer_broker.company_name')
    truck = serializers.ReadOnlyField(source='truck.unit_number')
    class Meta:
        model = Load
        fields = ['id', 'created_by', 'customer_broker', 'truck', 'created_date', 'load_id', 'trip_id', 'driver', 'co_driver', 'dispatcher', 'load_status', 'tags', 'equipment_type', 'trip_status', 'invoice_status', 'trip_bil_status', 'load_pay', 'driver_pay', 'total_pay', 'per_mile', 'mile', 'empty_mile', 'total_miles', 'flagged', 'flagged_reason', 'note', 'chat', 'rate_con', 'bol', 'pod', 'document', 'comercial_invoice']


class StopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = "__all__"


class OtherPaySerializers(serializers.ModelSerializer):
    class Meta:
        model = OtherPay
        fields = "__all__"


class CommoditiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Commodities
        fields = "__all__"


class LoadTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoadTags
        fields = "__all__"


class DriverTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DriverTags
        fields = "__all__"


class TrailerTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TrailerTags
        fields = "__all__"


class TruckTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TruckTags
        fields = "__all__"


class EmployeeTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTags
        fields = "__all__"


class DispatcherTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DispatcherTags
        fields = "__all__"

