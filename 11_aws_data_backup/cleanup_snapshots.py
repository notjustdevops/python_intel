from operator import itemgetter
import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-2")


def cleanup_snapshots():
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self']
    )

    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    '''for snap in snapshots['Snapshots']:
        print(snap['StartTime'])

    print('###############')

    for snap in sorted_by_date:
        print(snap['StartTime'])'''

    for snap in sorted_by_date[2:]:
        
        '''print(snap['SnapshotId'])
        print(snap['StartTime'])'''
        
        response = ec2_client.delete_snapshot(
            SnapshotId=snap['SnapshotId']
        )
        print(response)

schedule.every(40).seconds.do(cleanup_snapshots)
 
while True:
    schedule.run_pending()