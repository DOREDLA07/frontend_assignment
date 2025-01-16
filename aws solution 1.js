import json

def lambda_handler(event, context):
    # Extract numbers from the event object (Assumes event is a JSON with 'num1' and 'num2')
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)
    
    # Calculate the sum
    result = num1 + num2
    
    # Return the result in a JSON response format
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result
        })
    }
