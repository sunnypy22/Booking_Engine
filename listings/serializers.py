from rest_framework import serializers
from .models import Listing, Blocked, BookingInfo
from django.contrib.auth.models import User


class ListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class BookingInfoSerializer(serializers.ModelSerializer):
    listing = ListingSerializers(read_only=True)

    class Meta:
        model = BookingInfo
        fields = ['listing']


class BlockSerializers(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)
    info_booking = BookingInfoSerializer(read_only=True)

    def get_price(self, blocked):
        return blocked.info_booking.price

    class Meta:
        model = Blocked
        fields = ['price', 'info_booking']
