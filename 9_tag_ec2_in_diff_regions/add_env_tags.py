import boto3
import schedule

instance_ids_virginia = []
instance_ids_oregon = []

ec2_client_virginia = boto3.client('ec2', region_name="us-east-1")
ec2_resource_virginia = boto3.resource('ec2', region_name="us-east-1")

ec2_client_oregon = boto3.client('ec2', region_name="us-west-2")
ec2_resource_oregon = boto3.resource('ec2', region_name="us-west-2")

reservations_virginia = ec2_client_virginia.describe_instances()['Reservations']
for res in reservations_virginia:
    instances = res['Instances']
    for ins in instances:
        instance_ids_virginia.append(ins['InstanceId'])


response = ec2_resource_virginia.create_tags(
    Resources=instance_ids_virginia,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

reservations_oregon = ec2_client_oregon.describe_instances()['Reservations']
for res in reservations_oregon:
    instances = res['Instances']
    for ins in instances:
        instance_ids_oregon.append(ins['InstanceId'])


response = ec2_resource_oregon.create_tags(
    Resources=instance_ids_oregon,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
