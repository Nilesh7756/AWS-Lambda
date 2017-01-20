from __future__ import print_function # Python 2/3 compatibility
import boto3

client = boto3.client('dynamodb')

response_put = client.put_item(
    TableName='DynamoDB-Test',
    Item={

		'ID' : {
                               "N" : "2"
                       },
		
		'fName' : {
                                "S" : "Nilesh"
                        },
	
		'lName' : {
				"S" : "Suryavanshi"
			}
        }
  	


)
