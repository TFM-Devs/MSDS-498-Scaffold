import json

# import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import gzip
import awswrangler.secretsmanager as sm
import requests
import boto3

api_key = sm.get_secret_json("alphaVantageApiKey").get('api_key')

headers = {"apikey": api_key}
# https://www.alphavantage.co/query?function=RSI&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo
#                             /query?function=RSI&symbol=IBM&interval=weekly&time_period=60&series_type=open&datatype=json&apiKey=9%25VAY%26NUo
url = "https://www.alphavantage.co"
get_path = "/query?%s"

payload = {'function': 'RSI',
        'symbol': 'IBM',
        'interval': 'weekly',
        'time_period': '10',
        'series_type': 'open',
}
        
params = urllib.parse.urlencode(payload, safe='%&')
# print(params)
# print(get_path % params)
# print('')

conn = http.client.HTTPSConnection("alphavantage.co")
conn.request("GET", get_path % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
conn.close()
# response_data = data
print(data.decode("utf-8"))