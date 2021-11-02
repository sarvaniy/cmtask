from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from .tasks import exchange_rate_from_alphavantage, force_requesting_prices 
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import logging

#@api_view(['GET', 'POST'])
class TaskView(APIView):
    def get(self, request):
        try:
            print("entered")
            if not ExchangeRate.objects.filter(from_currency='BTC').exists():
                exchange_rate_from_alphavantage()
                print("hello")
            resp = ExchangeRate.objects.get(from_currency='BTC')
            serializer = ExchangeRateSerializer(resp, many=False)
            logging.info("resp", resp)
            logging.info("type", type(resp))
            return Response({"status": "success", "data": (serializer.data)}, status=status.HTTP_200_OK)
            #return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
            {
                'error_message': e
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request):
        try:
            from datetime import datetime
            resp = force_requesting_prices()
            today_resp = resp[datetime.today().strftime('%Y-%m-%d')]
            output = {datetime.today().strftime('%Y-%m-%d'): today_resp}
            return Response({"status": "success", "data": output}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
            {
                'error_message': e
            },
            status=status.HTTP_400_BAD_REQUEST
        )

