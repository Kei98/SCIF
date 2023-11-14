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
        purchase = Product.objects.get(pk=id)
    except Product.DoesNotExist:
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
        request.data._mutable = True
        request.data.update(serializer1.data)
        request.data._mutable = False
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)