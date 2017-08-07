from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer
from django.views.decorators.csrf import csrf_exempt

def index(request):
    rest_list = Restaurant.objects.order_by('-pub_date')
    context = {'rest_list': rest_list}
    return render(request,'food/index.html', context)

# Restframework
@csrf_exempt
def get_rest_list(request):
    """
    List all restaurants
    """
    rest_list = Restaurant.objects.order_by('-pub_date')
    serializer = RestaurantSerializer(rest_list, many=True)
    return JsonResponse(serializer.data, safe=False)
        
    
    