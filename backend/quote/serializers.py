from rest_framework import serializers
from .models import *
from service.serializers import ServiceDetsSerializer


class QuotesSerializer(serializers.ModelSerializer):
    _requestor = serializers.CharField(
        source='user.user_id.user_info_name', read_only=True)
    _quote_assigned_user = serializers.CharField(
        source='quote_assigned_user.user_id.user_info_name', read_only=True)

    class Meta:
        model = Quote
        fields = [
            'quote_id',
            'quote_request',
            'quote_on_behalf_of',
            'quote_date',
            'quote_active',
            '_requestor',
            '_quote_assigned_user'
        ]


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class QuoteAnswersSerializer(serializers.ModelSerializer):
    _user = serializers.CharField(
        source='user.user_id.user_info_name', read_only=True)
    service_detail = ServiceDetsSerializer(read_only=True)

    class Meta:
        model = QuoteAnswer
        fields = [
            'quote_answer_id',
            'quote_answer_description',
            'quote_answer_date',
            'quote_answer_active',
            'quote',
            '_user',
            'service_detail'
        ]


class QuoteAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteAnswer
        fields = '__all__'
