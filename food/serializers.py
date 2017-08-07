from rest_framework import serializers
from food.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'photo', 'tags', 'menu', 'pub_date')