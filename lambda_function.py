import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-counter-table')

def lambda_handler(event, context):
 response = table.update_item(
 Key={'id': 'visitor-count'},
 UpdateExpression='SET #count = if_not_exists(#count,:start) +:inc',
 ExpressionAttributeNames={'#count': 'count'},
 ExpressionAttributeValues={':inc': 1, ':start': 0},
 ReturnValues='UPDATED_NEW'
 )
 count = int(response['Attributes']['count'])
 return {
 'statusCode': 200,
 'headers': {
 'Access-Control-Allow-Origin': '*',
 'Access-Control-Allow-Headers': '*',
 'Access-Control-Allow-Methods': '*'
 },
 'body': json.dumps({'count': count})
 }
