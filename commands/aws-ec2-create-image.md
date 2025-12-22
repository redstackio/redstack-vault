---
id: b44c14e6-dfdf-4e4a-ab76-251ad1382f4a
name: aws-ec2-create-image
type: command
executor: bash
data: >
  aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME
  --description $AWS_AMI_DESCRIPTION
output: null
created_at: '2020-07-31T04:25:34.192231+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - AWS
  - EC2
  - AMI
verified: true
validated: true
---

# aws-ec2-create-image

## Command

```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION
```

## Description

This command creates an Amazon Machine Image (AMI) from a specified EC2 instance, capturing its current state including the root volume. By default, the instance will be rebooted to ensure a clean snapshot. Use this in post-exploitation scenarios to preserve compromised instance configurations for later replication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --instance-id $AWS_INSTANCE_ID | The ID of the EC2 instance to image (e.g., i-1234567890abcdef0) | Yes |
| --name $AWS_AMI_NAME | Name for the new AMI (e.g., "compromised-instance-2023-10-01") | Yes |
| --description $AWS_AMI_DESCRIPTION | Descriptive text for the AMI (e.g., "Snapshot of production server") | Yes |

## Examples

### Basic Usage

```bash
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "backup-ami" --description "Emergency backup"
```

### Advanced Usage

```bash
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "persistent-backdoor-ami" --description "Includes custom persistence mechanisms" --tag-specifications 'ResourceType=image,Tags=[{Key=Owner,Value=Attacker}]'
```

## Expected Output

```
{
    "ImageId": "ami-0abcdef1234567890",
    "RequestId": "req-12345678-90ab-cdef-1234-567890abcdef"
}
```

The output provides the AMI ID, which can be used to track creation status or share the image. The instance will stop and restart during the process.

## Related

- [[procedures/AWS-Create-EC2-AMI-Image]]
- [[commands/aws-ec2-create-image-no-reboot]]
