from django.urls import path
from .views import HomeView, DeviceDetailInfo, AddDeviceView, CategorySelect

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('device/<int:pk>', DeviceDetailInfo.as_view(), name='information'),
    path('add', AddDeviceView.as_view(), name='new_device'),
    path('category/<str:select>/', CategorySelect, name='category')

]
