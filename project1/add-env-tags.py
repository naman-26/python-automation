import boto3

# Paris region (eu-west-3)
ec2_client_paris = boto3.client('ec2', region_name="eu-west-3")
ec2_resource_paris = boto3.resource('ec2', region_name="eu-west-3")

instance_ids_paris = []

reservations_paris = ec2_client_paris.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instance_ids_paris.append(ins['InstanceId'])


ec2_resource_paris.create_tags(
    Resources=instance_ids_paris,
    Tagss=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]

)




