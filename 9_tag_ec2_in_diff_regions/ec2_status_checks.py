import boto3
import schedule


ec2_client = boto3.client('ec2', region_name="us-west-2")
ec2_resource = boto3.resource('ec2', region_name="us-west-2")



# Example for training
reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f"Status of the instance {instance['InstanceId']} is: {instance['State']['Name']}")

def check_instance_status():
    # It's possible to print 'InstanceState' and thats it.
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} \nwith instance status {ins_status} and system status is {sys_status}")
    print('######################\n')


schedule.every(10).seconds.do(check_instance_status)

while True:
    schedule.run_pending()