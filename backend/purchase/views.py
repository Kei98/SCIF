from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def purchase_list(request, format=None):
    purchases = Purchase.objects.all()
    serializer = PurchasesSerializer(purchases, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def purchase_post(request, format=None):
    serializer = PurchaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])
def purchase_detail(request, id, format=None):
    try:
        purchase = Purchase.objects.get(pk=id)
    except Purchase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PurchasesSerializer(purchase)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        purchase.purchase_active = 0
        serializer1 = PurchaseSerializer(purchase)
        request.data['_mutable'] = True
        request.data.update(serializer1.data)
        request.data['_mutable'] = False
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)
        
#Purchase Detail
@api_view(['GET'])
def purchase_det_list(request, format=None):
    purchase_det = PurchaseDetail.objects.all()
    serializer = PurchaseDetailsSerializer(purchase_det, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def purchase_det_post(request, format=None):
    serializer = PurchaseDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def purchase_det_detail(request, id, format=None):
    try:
        purchase_det = PurchaseDetail.objects.get(pk=id)
    except Purchase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PurchaseDetailsSerializer(purchase_det)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PurchaseDetail(purchase_det, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

