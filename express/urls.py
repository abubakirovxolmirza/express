from django.urls import path
from .views import DriverList, TruckList, TrailerList, DispatcherList, CustomerBrokerList, EmployeeList, LoadList, StopsList, OtherPayList, CommoditiesList
from .views import DriverDetail, TruckDetail, TrailerDetail, DispatcherDetail, CustomerBrokerDetail, EmployeeDetail, LoadDetail, StopsDetail, OtherPayDetail, CommoditiesDetail

urlpatterns = [
    path('driver/', DriverList.as_view()),
    path('truck/', TruckList.as_view()),
    path('trailer/', TrailerList.as_view()),
    path('dispatcher/', DispatcherList.as_view()),
    path('customer/', CustomerBrokerList.as_view()),
    path('employee/', EmployeeList.as_view()),
    path('load/', LoadList.as_view()),
    path('stop/', StopsList.as_view()),
    path('otherpay/', OtherPayList.as_view()),
    path('commoditie/', CommoditiesList.as_view()),

    path('drivers/<int:pk>/', DriverDetail.as_view()),
    path('trucks/<int:pk>/', TruckDetail.as_view()),
    path('trailers/<int:pk>/', TrailerDetail.as_view()),
    path('dispatchers/<int:pk>/', DispatcherDetail.as_view()),
    path('customers/<int:pk>/', CustomerBrokerDetail.as_view()),
    path('employees/<int:pk>/', EmployeeDetail.as_view()),
    path('loads/<int:pk>/', LoadDetail.as_view()),
    path('stops/<int:pk>/', StopsDetail.as_view()),
    path('otherpays/<int:pk>/', OtherPayDetail.as_view()),
    path('commodities/<int:pk>/', CommoditiesDetail.as_view()),
]
