import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import gzip
import awswrangler.secretsmanager as sm
import requests
import boto3

api_key = sm.get_secret_json("alphaVantageApiKey").get('api_key')

url = "https://www.alphavantage.co/query"
get_path = "/query?%s"

pop_stocks = ["TSLA", "AAPL", "AMZN",  "MSFT", "NIO", "NVDA", "MRNA", "NKLA"]

all_stk_rsi_list = []

payload = {'function': 'RSI',
            'symbol': 'IBM',
            'interval': '60min',
            'time_period': '10',
            'series_type': 'open',
            'apikey' : api_key
        }
        
params = urllib.parse.urlencode(payload, safe='%&')

json_data = requests.get(url, params).json()

metadata = json_data["Meta Data"]
tech_analysis = json_data['Technical Analysis: RSI']
symbol = metadata['1: Symbol']

for date_item in tech_analysis:
    tech_analysis[date_item]['symbol'] = symbol
    tech_analysis[date_item]['trade_date'] = date_item
    all_stk_rsi_list.append(tech_analysis[date_item])
    # print(tech_analysis[date_item])
    # for tekitem in date_item:
    #     tekitem['symbol'] = metadata['1: Symbol']
    # # date_item['trade_date'] = date_item  

print(all_stk_rsi_list)
        
        
       