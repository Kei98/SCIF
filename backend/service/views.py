from django.db import IntegrityError
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def service_list(request, format=None):
    if request.method == 'GET':
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, id, format=None):
    try:
        service = Service.objects.get(pk=id)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            service.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        except IntegrityError as e:
            service.service_active = 0
            serializer1 = ServiceSerializer(service)
            request.data['_mutable'] = True
            request.data.update(serializer1.data)
            request.data['_mutable'] = False
            serializer = ServiceSerializer(service, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET'])
def service_det_list(request, format=None):
    services_det = ServiceDetail.objects.all()
    serializer = ServiceDetsSerializer(services_det, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def service_det_post(request, format=None):
    serializer = ServiceDetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def service_det_detail(request, id, format=None):
    try:
        service_det = ServiceDetail.objects.get(pk=id)
    except ServiceDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceDetsSerializer(service_det)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ServiceDetSerializer(service_det, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        service_det.user_active = 0
        serializer1 = ServiceDetSerializer(service_det)
        request.data['_mutable'] = True
        request.data.update(serializer1.data)
        request.data['_mutable'] = False
        serializer = ServiceDetSerializer(service_det, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)
