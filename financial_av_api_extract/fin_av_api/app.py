import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import awswrangler.secretsmanager as sm
import requests
import boto3
from os import listdir
from os.path import isfile, join

## Global
s3_client = boto3.client("s3")
LOCAL_FILE_SYS = "/tmp"
S3_BUCKET = "financial-group-data" 

def upload_file_to_s3(upload_file, file_name):
    result = s3_client.upload_file(upload_file, S3_BUCKET, file_name)
    return result

def parse_data(dict_data,tek_ind):
    return f'{dict_data["symbol"]},{dict_data["trade_date"]},{dict_data[tek_ind]}\n'


def write_to_local(tek_ind_list, tek_ind_file_nm, tek_ind, loc=LOCAL_FILE_SYS):
    file_name = loc + "/" + tek_ind_file_nm
    file_header = f"symbol,trade_date,{tek_ind}\n"
    with open(file_name, "w") as file:
        file.write(file_header)
        for tek_ind_dict in tek_ind_list:
            file.write(parse_data(tek_ind_dict,tek_ind))
    return file_name


def etl_list(tek_ind_json_data, tek_ind_list, tek_ind, sec_sym):
    analysis_name = 'Technical Analysis: '+ tek_ind
    #metadata = tek_ind_json_data["Meta Data"]
    tech_analysis = tek_ind_json_data[analysis_name]
    #symbol = metadata['1: Symbol']

    for date_item in tech_analysis:
        tech_analysis[date_item]['symbol'] = sec_sym
        tech_analysis[date_item]['trade_date'] = date_item
        tek_ind_list.append(tech_analysis[date_item])
    
    return tek_ind_list

def get_data(funct, sec_sym):
   
    url = "https://www.alphavantage.co/query"
    api_key = sm.get_secret_json("alphaVantageApiKey").get('api_key')

    payload = {'function': funct,
            'symbol': sec_sym,
            'interval': '60min',
            'time_period': '10',
            'series_type': 'open',
            'apikey' : api_key
        }
        
    params = urllib.parse.urlencode(payload, safe='%&')

    response_json = requests.get(url, params).json()
    
    return response_json

def lambda_handler(event, context):
    ## Play the role of evnt variables
    pop_stocks_list = event["stocks"]
    tek_ind         = event["technical_indicator"]
    tek_ind_file_nm = event["data_file"]
    #######################################
    all_stk_tek_ind_list = []
    
    for stk_sym in pop_stocks_list:
        tek_ind_json_data =get_data(tek_ind, stk_sym)
        all_stk_tek_ind_list = etl_list(tek_ind_json_data, all_stk_tek_ind_list, tek_ind, stk_sym)

    file_to_upload = write_to_local(all_stk_tek_ind_list, tek_ind_file_nm, tek_ind)
    result_returned = upload_file_to_s3(file_to_upload, tek_ind_file_nm)
    
    return {
      "statusCode": 200,
      "body": json.dumps({
      "message": "hello world",
    # "location": ip.text.replace("\n", "")
    }),
    }