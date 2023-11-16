# from django.db import IntegrityError
# from .models import *
# from .serializers import *
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET'])
# def quote_list(request, format=None):
#     quotes = Quote.objects.all()
#     serializer = QuotesSerializer(quotes, many=True)
#     return Response(serializer.data)

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
    

