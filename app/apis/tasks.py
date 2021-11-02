from app.celery import app, task
from .models import ExchangeRate
import requests, os

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    #sender.add_periodic_task(30.0, exchange_rate_from_alphavantage.s(), name='add evry 30')
    sender.add_periodic_task(crontab(minute=0, hour="*/1"), exchange_rate_from_alphavantage.s())

@task
def exchange_rate_from_alphavantage():
    print('Fetching Exchange Rate from Alphavantage API with API_KEY for BTC/USD')
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    api_key = os.environ.get("API_KEY")
    url = base_url+"&from_currency=BTC&to_currency=USD&apikey="+api_key

    req_ob = requests.get(url)

    # result contains list of nested dictionaries
    result = req_ob.json()

    print(" Result before parsing the json data :\n", result)
    
    #create/update entry for BTC/USD in exchangerate table
    if not ExchangeRate.objects.filter(from_currency='BTC').exists():	
        ExchangeRate.objects.create(from_currency = "BTC",to_currency = "USD",
            ex_rate = result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    else:
        ExchangeRate.objects.filter(from_currency='BTC').update(ex_rate=result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    print("Done")


def force_requesting_prices():
    print('hitting the server')
    api_key = os.environ.get("API_KEY")
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey='+ api_key
    r = requests.get(url)
    output = r.json()['Time Series (Digital Currency Daily)']
    return output

