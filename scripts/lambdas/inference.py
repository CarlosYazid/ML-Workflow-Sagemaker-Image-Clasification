import json
import boto3
import base64

# Fill this in with the name of your deployed model
ENDPOINT = 'ENDPOINT_NAME'

sagemaker_runtime = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])
    
    # Make a prediction:
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image
    )

    inferences = response['Body'].read()
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }