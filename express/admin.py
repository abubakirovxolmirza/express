from django.contrib import admin
from .models import Driver, Truck, Trailer, Employee, Dispatcher, CustomerBroker, Load, Stops, OtherPay, Commodities, TrailerTags, DriverTags, TruckTags, DispatcherTags, EmployeeTags, LoadTags

# Register your models here.
admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(Trailer)
admin.site.register(Employee)
admin.site.register(Dispatcher)
admin.site.register(CustomerBroker)
admin.site.register(Load)
admin.site.register(Stops)
admin.site.register(OtherPay)
admin.site.register(Commodities)
admin.site.register(TrailerTags)
admin.site.register(TruckTags)
admin.site.register(DispatcherTags)
admin.site.register(DriverTags)
admin.site.register(EmployeeTags)
admin.site.register(LoadTags)


