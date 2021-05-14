import boto3
import click
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr
import pandas as pd
import json

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

@click.command(help='this is just a basic player search app')
@click.option('--player', prompt="I need the player name", help="Need primary_key")

def player_metric(player):
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table('MarketMoversFromS3')
   response = table.scan(
       FilterExpression=Attr('Player').eq(player))
   
   df = pd.DataFrame(response['Items'])
   df = df[['Player','Card','Start_Avg','End_Avg','Percent_Change','Sales_Volume']]
   print(df)

if __name__ == '__main__':
    player_metric()

