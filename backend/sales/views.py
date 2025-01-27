from django.db import IntegrityError, transaction
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import requests
from django.shortcuts import render
from django.db import connection
from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework.views import APIView

# @api_view(['GET'])
# def quote_list(request, format=None):
#     quotes = Quote.objects.all()
#     serializer = QuotesSerializer(quotes, many=True)
#     return Response(serializer.data)

# InventoryReportSerializer


# @api_view(['GET'])
# def inventory_list(request, format=None):
#     inventory = SalesDetail.objects.raw("SELECT s.* FROM sales_detail s WHERE s.sales_id in (SELECT sales_id FROM sales WHERE sales_status_id != 1)")
#     inventory_purchase = PurchaseDetail.objects.raw("SELECT p.* FROM purchase_detail p WHERE p.purchase_id in (SELECT purchase_id FROM purchase WHERE purchase_active = true)")
#     inv_list = list(chain(inventory, inventory_purchase))
#     print(inv_list)
#     serializer = InventoryReportSerializer(inv_list, many=True)
#     return Response(serializer.data)

class CreateInventoryView(viewsets.ModelViewSet):
    with connection.cursor() as cursor:
        cursor.callproc('get_inventory_report')
        result= cursor.fetchall()
        results = []
        for row in result:
            result_dict= dict(zip([col[0] for col in cursor.description], row))
            print('cursor.description')
            print(cursor.description)
            results.append(result_dict)
        print('results')
        print(results)

    # return Response(results)
        queryset = results
        serializer_class = InventoryReportSerializer

def inventoryView(request, format=None):
    with connection.cursor() as cursor:
        cursor.callproc('get_inventory_report')
        result= cursor.fetchall()
        results = []
        for row in result:
            result_dict= dict(zip([col[0] for col in cursor.description], row))
            print('cursor.description')
            print(cursor.description)
            results.append(result_dict)
        print('results')
        print(results)
        serialized_data = serialize('json', results)
        return JsonResponse(serialized_data, safe=False)


# @api_view(['GET'])
# def sales_report(request, format=None):
#     report = Sales.objects.exclude(sales_status_id=1)
#     print(report)
#     serializer = SalesReportSerializer(report, many=True)
#     return Response(serializer.data)

class CreateSalesView(viewsets.ModelViewSet):
    with connection.cursor() as cursor:
        cursor.callproc('get_purchase_sale_report')
        result= cursor.fetchall()
        results = []
        for row in result:
            result_dict= dict(zip([col[0] for col in cursor.description], row))
            results.append(result_dict)

        queryset = results
        serializer_class = SalesReportSerializer

def salesView(request, format=None):
    with connection.cursor() as cursor:
        cursor.callproc('get_purchase_sale_report')
        result= cursor.fetchall()
        results = []
        for row in result:
            result_dict= dict(zip([col[0] for col in cursor.description], row))
            results.append(result_dict)
        serialized_data = serialize('json', results)
        return JsonResponse(serialized_data, safe=False)

@api_view(['GET'])
def payment_method_get(request, format=None):
    payment_method = PaymentMethod.objects.all()
    serializer = PaymentMethodSerializer(payment_method, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sales_get(request, format=None):
    sale = Sales.objects.all()
    serializer = SalessSerializer(sale, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sales_get_or(request, format=None):
    sale = Sales.objects.all()
    serializer = SalesSerializerGet(sale, many=True)
    return Response(serializer.data)

class CreateSaleView(APIView):
    @transaction.atomic
    def post(self, request):
        sales_data = request.data.get('sales')
        sales_details_data = request.data.get('sales_details')

        # Validate and save the Sales object
        sales_serializer = SalesSerializer(data=sales_data)
        if not sales_serializer.is_valid():
            return Response(sales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        sale = sales_serializer.save()

        # Validate and save the SalesDetail objects
        for detail in sales_details_data:
            detail['sales'] = sale.sales_id  # Link SalesDetail to the created Sale
            sales_detail_serializer = SalesDetSerializer(data=detail)
            if not sales_detail_serializer.is_valid():
                return Response(sales_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            sales_detail_serializer.save()

        return Response({'message': 'Sale created successfully!'}, status=status.HTTP_201_CREATED)

class SalesListView(APIView):
    def get(self, request):
        sales = Sales.objects.all()
        serializer = SalesSerializer(sales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, sales_id):
        try:
            sale = Sales.objects.get(id=sales_id)
            if sale.sales_status < 5:
                sale.sales_status_id = 1
                serializer1 = SalesSerializer(user)
                request.data['_mutable'] = True
                request.data.update(serializer1.data)
                request.data['_mutable'] = False
                serializer = SalesSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'Sale cancelled successfully'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'Sale cannot be cancelled after it was delivered'}, status=status.HTTP_200_BAD_REQUEST)
        except Sales.DoesNotExist:
            return Response({'error': 'Sale not found'}, status=status.HTTP_404_NOT_FOUND)

class SalesDetailsView(APIView):
    def get(self, request, sales_id):
        details = SalesDetail.objects.filter(sales_id=sales_id)
        serializer = SalesDetsSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SalesDetailUpdateView(APIView):
    def put(self, request, detail_id):
        try:
            detail = SalesDetail.objects.get(sales_detail_id=detail_id)
        except SalesDetail.DoesNotExist:
            return Response({'error': 'Sales detail not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SalesDetsSerializer(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)