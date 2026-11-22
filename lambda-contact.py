import json
import boto3

ses = boto3.client('ses', region_name='af-south-1')

def lambda_handler(event, context):
 body = json.loads(event.get('body', '{}'))
 name = body.get('name', '')
 email = body.get('email', '')
 message = body.get('message', '')

 ses.send_email(
 Source='bradleydms6@gmail.com',
 Destination={'ToAddresses': ['bradleydms6@gmail.com']},
 Message={
 'Subject': {'Data': f'New Contact from {name}'},
 'Body': {'Text': {'Data': f'From: {name} ({email})\n\n{message}'}}
 }
 )

 return {
 'statusCode': 200,
 'headers': {'Access-Control-Allow-Origin': '*'},
 'body': json.dumps({'message': 'Message sent!'})
 }
