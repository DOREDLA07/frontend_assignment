import json
import base64
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the base64-encoded document from the event
    file_content_base64 = event.get('file_content', '')
    file_name = event.get('file_name', 'document.pdf')
    bucket_name = event.get('bucket_name', 'your-bucket-name')
    
    if not file_content_base64 or not file_name or not bucket_name:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing required parameters (file_content, file_name, or bucket_name)'})
        }

    try:
        # Decode the base64 file content
        file_content = base64.b64decode(file_content_base64)

        # Upload the file to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType='application/pdf'  # Assuming a PDF; adjust as needed for other file types
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully'})
        }
    
    except NoCredentialsError:
        return {
            'statusCode': 403,
            'body': json.dumps({'error': 'AWS credentials not found'})
        }
    except PartialCredentialsError:
        return {
            'statusCode': 403,
            'body': json.dumps({'error': 'Incomplete AWS credentials'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
