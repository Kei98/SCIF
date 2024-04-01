# from django.db import IntegrityError
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Value, CharField
from django.db.models.functions import Concat


@api_view(['GET', 'POST'])
def product_sheet_list(request, format=None):
    if request.method == 'GET':
        product_sheets = ProductSpecSheet.objects.all()
        serializer = ProductSpecSheetSerializer(product_sheets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSpecSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def product_list(request, format=None):
    products = Product.objects.all()
    # data_with_labels = Product.objects.annotate(custom_field=Concat(
    #     Value('product_id: '), 'ID',
    #     Value('product_name: '), 'Name',
    #     Value('product_description: '), 'Description',
    #     Value('product_image: '), 'Image',
    #     Value('product_i: '), 'Info',
    #     Value('_spec_sheet: '), 'Specs Sheet',
    #     Value('product_active: '), 'Active',
    #     output_field=CharField()
    # )
    # )
    # print(data_with_labels)
    serializer = ProductsSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_post(request, format=None):
    serializer = ProductSerializer(data=request.data)
    print('prod serializer')
    print(serializer)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id, format=None):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.product_active = 0
        serializer1 = ProductSerializer(product)
        request.data['_mutable'] = True
        request.data.update(serializer1.data, partial=True)
        request.data['_mutable'] = False
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)

# Product Info


@api_view(['GET', 'POST'])
def product_info_list(request, format=None):
    if request.method == 'GET':
        product_info = ProductInfo.objects.all()
        serializer = ProductInfoSerializerGet(product_info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductInfoSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print('enters is valid')
            serializer.save()
            print('passes save')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def product_info_detail(request, id, format=None):
    try:
        product_info = ProductInfo.objects.get(pk=id)
    except ProductInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductInfoSerializer(product_info)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductInfoSerializer(product_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('Deleting is not supported', status=status.HTTP_400_BAD_REQUEST)
