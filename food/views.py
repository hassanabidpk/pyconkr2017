from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

def index(request):
    res_list = Restaurant.objects.order_by('-pub_date')
    context = {'res_list': res_list}
    return render(request,'food/index.html', context)