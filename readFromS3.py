import boto3
import json
import pickle
import cPickle
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

s3 = boto3.resource('s3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

#bucket = s3.Bucket('test-bucket-ttdsgroup')
content_object = s3.Object('test-bucket-ttdsgroup', 'index.pkl')
body_string = content_object.get()['Body'].read()
positive_model_data = cPickle.loads(body_string)
print(json.dumps(positive_model_data, indent=4))
