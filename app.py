import boto3

# Create a Lambda client
client = boto3.client('lambda')

# Create a Lambda function
response = client.create_function(
    FunctionName='jrp',  # Replace with your desired function name
    Runtime='python3.9',  # Correct runtime
    Role='arn:aws:iam::908027386826:role/lamda-admin',  # Correct IAM role ARN
    Handler='lambda.lambda_handler',  # Specify the entry point function in your code
    Code={
        'S3Bucket': 'asdfghjknk',  # Correct bucket name
        'S3Key': 'lambda.zip'  # Correct file name in the bucket
    },
    Description='A test Lambda function',
    Timeout=15,  # Optional: Set timeout in seconds (default is 3)
    MemorySize=128  # Optional: Memory size in MB (default is 128)
)

print("Lambda function created:", response)
