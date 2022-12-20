from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Device, Category
from .forms import DeviceForm


class HomeView(ListView):
    model = Device
    template_name = 'main/index.html'


class DeviceDetailInfo(DetailView):
    model = Device
    template_name = 'main/device_info.html'


class AddDeviceView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'main/add_device.html'


class CategoryView(CreateView):
    model = Category
    template_name = 'main/add_device.html'
    fields = '__all__'



def CategorySelect(request, select):
    category_device = Device.objects.filter(category=select)
    return render(request, 'main/category.html', {'select': select, 'category_device': category_device})