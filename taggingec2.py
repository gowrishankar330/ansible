import boto3

def tag_ec2_instance(instance_id, tags):
    ec2 = boto3.client('ec2')
    ec2.create_tags(
        Resources=[instance_id],
        Tags=[{"Key": key, "Value": value} for key, value in tags.items()])
    print(f"Tagged {instance_id} with {tags}")

# Example usage
tag_ec2_instance("i-0abc123def456gh78", {
    "Environment": "Production",
    "Owner": "DevOps",
    "Purpose": "WebServer"
})