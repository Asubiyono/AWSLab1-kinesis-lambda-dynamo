import json
import csv
import boto3
import logging
from io import StringIO
 
# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def convert_str_to_int(value, default=0):
    """Convert string to integer, handling empty strings and conversion errors."""
    try:
        return int(float(value)) if value.strip() else default
    except ValueError as e:
        logger.warning(f"ValueError converting to int: {e}")
        return default
 
def convert_str_to_float(value, default=0.0):
    """Convert string to float, handling empty strings and conversion errors."""
    try:
        return float(value) if value.strip() else default
    except ValueError as e:
        logger.warning(f"ValueError converting to float: {e}")
        return default
 
def convert_to_correct_type(ride):
    # Convert fields to their appropriate types
    for key in ['vendor_id', 'rate_code', 'passenger_count', 'pickup_location_id', 'dropoff_location_id']:
        ride[key] = convert_str_to_int(ride[key])
 
    for key in ['trip_distance', 'fare_amount', 'tip_amount', 'total_amount']:
        ride[key] = convert_str_to_float(ride[key])
 
    return ride

def lambda_handler(event, context):
    # Set the region
    region_name = 'us-east-1'
 
    # Initialize AWS clients with the specified region
    s3_client = boto3.client('s3', region_name=region_name)
    kinesis_client = boto3.client('kinesis', region_name=region_name)
 
    # Extract bucket name and file name from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
 
    logger.info(f"Received event for file: {file_name} in bucket: {bucket_name}")
 
    # Get the file from S3
    try:
        obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        file_content = obj['Body'].read().decode('utf-8')
    except Exception as e:
        logger.error(f"Error getting file {file_name} from bucket {bucket_name}: {e}")
        raise e
 
    # Read the file content using csv.DictReader
    csv_data = StringIO(file_content)
    csv_reader = csv.DictReader(csv_data)
 
    # Process and send each line of the CSV to Kinesis
    counter = 0
    for row in csv_reader:
        try:
            ride = convert_to_correct_type(row)
 
            response = kinesis_client.put_record(
                StreamName="taxi_trips",
                Data=json.dumps(ride),
                PartitionKey=str(hash(ride['pickup_datetime']))
            )
 
            counter += 1
 
            # Check response status
            if response['ResponseMetadata']['HTTPStatusCode'] != 200:
                logger.error('Error sending message to Kinesis:', response)
 
        except Exception as e:
            logger.error(f"Error processing record {row}: {e}")
 
    logger.info(f"Finished processing. Total records sent: {counter}")
    return {
        'statusCode': 200,
        'body': json.dumps(f"Processed {counter} records from {file_name} in S3 bucket {bucket_name}.")
    }