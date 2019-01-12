import boto3
import boto.s3
import sys
from boto.s3.key import Key

print "Connecting to S3"

#Should be kept secret, but these are for the ttds-group-user account,
#who is in the ttds-team group which only has s3 access - so an attacker
#can't do tooo much damage I don't think
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

s3 = boto3.resource('s3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

test_binary_data = b'This is some text data from S3 :)'

object = s3.Object('test-bucket-ttdsgroup', 'testfile.txt')
object.put(Body=test_binary_data)
