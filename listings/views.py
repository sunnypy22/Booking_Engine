from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Listing, Blocked
from .serializers import ListingSerializers, BlockSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


@api_view(['GET'])
def listing(request):
    listing_list = Listing.objects.all()
    serializer = ListingSerializers(listing_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def booking(request):
    check_in = ''
    check_out = ''
    max_price = ''
    if 'check_in' in request.GET and 'check_out' in request.GET and 'max_price' in request.GET:
        check_in = request.GET['check_in']
        check_out = request.GET['check_out']
        max_price = request.GET['max_price']

    data = Blocked.objects.filter(start_date__gte=check_in,end_date__lte=check_out,info_booking__price__lt=max_price)
    serializer = BlockSerializers(data, many=True)
    return Response(serializer.data)
