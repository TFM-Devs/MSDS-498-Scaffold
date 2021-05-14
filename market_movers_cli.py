import boto3
import click

__TableName__ = "MarketMoversFromS3"
Primary_Column_Name = 'PrimaryKey'
Primary_Key = 'Aaron Gordon2014 Prizm Base Raw'

Columns = ['PrimaryKey', 
'Card', 
'Change', 
'End_Avg', 
'Maximum',
'Minimum',
'Percent_Change',
'Player',
'Sales_Volume',
'Start_Avg',
'Total_of_Sales'
]

#client = boto3.client('dynamodb')
db = boto3.resource('dynamodb')

table = db.Table(__TableName__)

@click.command(help='this is just a basic player search app')
@click.option('--primary_key', prompt="I need the primary key value", help="Need primary_key")
@click.option('--player_name', prompt="I need the name of the player", help="Need name")
@click.option('--metric', prompt='I need the name of the metric', help="Need metric")

def player_metric(primary_key, player_name, metric):
   response = table.get_item(
       Key={
           Primary_Column_Name: primary_key
       }
     )
   print(response['Item'][metric])
   
   
    #print(response["Player"])
    #print(response[metric])
    
#def player_metric(player_name, metric):
#    response = table.scan(
#        FilterExperssion = table.attr('Player').eq('Allen Iverson'))
#    print(response)

    #print(response["Player"])
    #print(response[metric])

if __name__ == '__main__':
    player_metric()

