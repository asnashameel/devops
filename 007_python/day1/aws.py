import boto3
def create_ec2_instance():
    try:
        print("creating ec2 to instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-08b1d20c6a69a7100",
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "t3.micro",
            KeyName = "vm-key"
        )
    except Exception as e:
        print(e)
create_ec2_instance()