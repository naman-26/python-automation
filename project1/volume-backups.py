import boto3
import schedule

ec2_client = boto3.client('ec2')


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        # Creating snapshot of volumes with Environment tag prod using filter
        Filters=[
            {
                'Name': 'tag:Environment',
                'Values': ['prod']
            }
        ]
    )

    for volume in volumes:
        new_snapshot = ec2_client.create_snapshot(
            VolumnId=volume['VolumeId']
        )
        print(new_snapshot)


schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()