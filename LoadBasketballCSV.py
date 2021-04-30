import csv
import boto3

def lambda_handler(event, context):
    region='us-east-2'
    reclist=[]
    try:
        s3 = boto3.client('s3')
        dyndb = boto3.client('dynamodb', region_name = region)
        confile = s3.get_object(Bucket='marketmovers', Key='market-movers-export-basketball.csv')
        
        reclist = confile['Body'].read().split('\n')
        firstrecord = True
        
        csv_reader = csv.reader(reclist,delimeter = ',', quotechar='"')
        for row in csv_reader:
            if (firstrecord):
                firstrecord=False
                continue
        response = dyndb.put_item(
            TableName = 'marketmoversbasketball',
            Item = {
            'PrimaryKey': {'S': str(PrimaryKey)},
            'Player': {'S': str(Player)},
            'Card': {'S': str(Card)},
            'Change': {'N': float(Change)},
            'Percent Change': {'N': float(Percent_Change)},
            'Start Avg': {'N': float(Start_Avg)},
            'End Avg': {'N': float(End_Avg)},
            'Total of Sales':{'N': int(Total_of_Sales)},
            'Minimum Sale Price': {'N': float(Minimum_Sale_Price)},
            'Maximum Sale Price': {'N': float(Maximum_Sale_Price)},
            'Sales Volume': {'N': int(Sales_Volume)}
            })
        print('Put Succeeded')
    except Exception:
        print(str(Exception))

