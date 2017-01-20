#from __future__ import print_function # Python 2/3 compatibility
import boto3

client = boto3.client('dynamodb')

response = client.get_item(
    TableName='DynamoDB-Test',
    Key={
		'ID' : {
				"N" : "1"
			}
	}	
)
#response = client.describe_table(
#    TableName='DynamoDB-Test'
#)
print response
