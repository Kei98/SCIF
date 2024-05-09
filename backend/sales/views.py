from django.db import IntegrityError
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions
import requests
from django.shortcuts import render
from django.db import connection
from django.core.serializers import serialize
from django.http import JsonResponse
# from django.db.models import Q
# from purchase.models import PurchaseDetail
# from itertools import chain

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


# def displaytable(request):
#     jtables=requests.get('http://127.0.0.1:8000/inventoryreport')
#     jsonobj=jtables.json()
#     return render(request, 'Index.html', {"inventoryreport": jsonobj})

@api_view(['GET'])
def sales_report(request, format=None):
    report = Sales.objects.filter(sales_status.sales_status_id !="1")
    print(report)
    serializer = InventoryReportSerializer(report, many=True)
    return Response(serializer.data)

# @api_view(['GET','POST'])
# def quote_post(request, format=None):
#     serializer = QuoteSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def quote_detail(request, id, format=None):
#     try:
#         quote = Quote.objects.get(pk=id)
#     except Quote.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = QuotesSerializer(quote)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = QuoteSerializer(quote, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         try:
#             quote.delete()
#             return Response(status.HTTP_204_NO_CONTENT)
#         except IntegrityError as e:
#             quote.quote_active = 0
#             serializer1 = QuoteSerializer(quote)
#             request.data['_mutable'] = True
#             request.data.update(serializer1.data)
#             request.data['_mutable'] = False
#             serializer = QuoteSerializer(quote, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)
#         return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


# #Quote Answer
# @api_view(['GET'])
# def quote_answer_list(request, format=None):
#     quote_ans = QuoteAnswer.objects.all()
#     serializer = QuoteAnswersSerializer(quote_ans, many=True)
#     return Response(serializer.data)

# @api_view(['GET','POST'])
# def quote_answer_post(request, format=None):
#     serializer = QuoteAnswerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def quote_answer_detail(request, id, format=None):
#     try:
#         quote_ans = QuoteAnswer.objects.get(pk=id)
#     except QuoteAnswer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = QuoteAnswersSerializer(quote_ans)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = QuoteAnswerSerializer(quote_ans, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response('Deleting is not supported', status=status.HTTP_400_BAD_REQUEST)


