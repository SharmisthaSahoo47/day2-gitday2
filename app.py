mport json
import boto3

def lambda_handler(event, context):
        client = boto3.client('ec2')
            response = client.run_instances(
                            ImageId='ami-0614680123427b75e',
                                    InstanceType='t2.micro',
                                            KeyName='aws',
                                                    MaxCount=2,
                                                            MinCount=1
                                                                )
                return {
                                'statusCode': 200,
                                        'body': json.dumps(f"Launched instance ID: {response['Instances'][0]['InstanceId']}")
                                            }

