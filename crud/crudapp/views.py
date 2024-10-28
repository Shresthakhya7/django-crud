from django.shortcuts import render
from .models import Destinations, Guide
from .serializers import DestinationSerializer, GuideSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics



class guide_list(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

class guide_list_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer 



# Create your views here.
@api_view(['GET'])
def  destinations_list(request):
    destination  =Destinations.objects.all()
    serializer=DestinationSerializer(destination,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_by_id(request,pk):
    try:
        destination = Destinations.objects.get(pk=pk)
    except Destinations.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=DestinationSerializer(destination)
    return Response(serializer.data)


@api_view(['POST'])
def post_destinations(request):
    serializer=DestinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_destinations(request,pk):
    try:
        destination = DestinationSerializer.objects.get(pk=pk)
    except Destinations.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=DestinationSerializer(destination,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






