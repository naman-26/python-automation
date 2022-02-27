import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2')

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['prod']
        }
    ]
)

for volume in volumes['Volumes']:
    snapshots = ec2_client.describe_snapshots(
        OwenerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume['VolumeId']]
            }
        ]
    )

    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    for snap in sorted_by_date[2:]:
        # delete snapshot expect 2 recent version
        ec2_client.delete_snapshots(
            SnapshotId=snap['SnapShotId']
        )



