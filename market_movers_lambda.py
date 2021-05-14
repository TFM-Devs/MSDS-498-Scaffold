import boto3
s3_client = boto3.client("s3")
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MarketMoversFromS3')

#read data from s3 bucket
def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    market_movers_basketball = data.split("\n")
    
    for player in market_movers_basketball:
        print(player)
        player_data = player.split(",")
        
#write data to dynamodb
        table.put_item(
            Item = {
                "PrimaryKey": player_data[0],
                "Player": player_data[1],
                "Card": player_data[2],
                "Change": player_data[3],
                'Percent_Change': player_data[4],
                'Start_Avg': player_data[5],
                'End_Avg': player_data[6],
                'Total_of_Sales': player_data[7],
                'Minimum': player_data[8],
                'Maximum': player_data[9],
                'Sales_Volume': player_data[10]
            }
            )

        
        