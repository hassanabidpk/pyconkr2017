from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

def index(request):
    rest_list = Restaurant.objects.order_by('-pub_date')
    context = {'rest_list': rest_list}
    return render(request,'food/index.html', context)