from django.urls import path
from .views import DriverList, TruckList, TrailerList, DispatcherList, CustomerBrokerList, EmployeeList, LoadList, StopsList, OtherPayList, CommoditiesList, DriverTagsList, TruckTagsList, TrailerTagsList, EmployeeTagsList, DispatcherTagsList, LoadTagsList
from .views import DriverDetail, TruckDetail, TrailerDetail, DispatcherDetail, CustomerBrokerDetail, EmployeeDetail, LoadDetail, StopsDetail, OtherPayDetail, CommoditiesDetail, DriverTagsDetail, TruckTagsDetail, TrailerTagsDetail, EmployeeTagsDetail, DispatcherTagsDetail, LoadTagsDetail

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
    path('loadtag/', LoadTagsList.as_view()),
    path('drivertag/', DriverTagsList.as_view()),
    path('trucktag/', TruckTagsList.as_view()),
    path('trailertag/', TrailerTagsList.as_view()),
    path('dispatchertag/', DispatcherTagsList.as_view()),
    path('employeetag/', EmployeeTagsList.as_view()),

    path('driver/<int:pk>/', DriverDetail.as_view()),
    path('truck/<int:pk>/', TruckDetail.as_view()),
    path('trailer/<int:pk>/', TrailerDetail.as_view()),
    path('dispatcher/<int:pk>/', DispatcherDetail.as_view()),
    path('customer/<int:pk>/', CustomerBrokerDetail.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
    path('load/<int:pk>/', LoadDetail.as_view()),
    path('stop/<int:pk>/', StopsDetail.as_view()),
    path('otherpay/<int:pk>/', OtherPayDetail.as_view()),
    path('commoditie/<int:pk>/', CommoditiesDetail.as_view()),
    path('loadtag/<int:pk>/', LoadTagsDetail.as_view()),
    path('drivertag/<int:pk>/', DriverTagsDetail.as_view()),
    path('dispatchertag/<int:pk>/', DispatcherTagsDetail.as_view()),
    path('trucktag/<int:pk>/', TruckTagsDetail.as_view()),
    path('trailertag/<int:pk>/', TrailerTagsDetail.as_view()),
    path('employeetag/<int:pk>/', EmployeeTagsDetail.as_view()),

]
