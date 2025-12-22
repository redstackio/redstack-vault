---
id: 268e8cc6-88b3-4cbf-944e-857810a10091
name: aws-ec2-create-image-no-reboot
type: command
executor: bash
data: >
  aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME
  --description $AWS_AMI_DESCRIPTION --no-reboot
output: null
created_at: '2020-07-31T04:25:34.192365+00:00'
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

# aws-ec2-create-image-no-reboot

## Command

```bash
aws ec2 create-image --instance-id $AWS_INSTANCE_ID --name $AWS_AMI_NAME --description $AWS_AMI_DESCRIPTION --no-reboot
```

## Description

This command creates an AMI from an EC2 instance without rebooting it, allowing the instance to remain operational during the snapshot process. This is useful for maintaining stealth in active compromises where stopping the instance could trigger alerts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --instance-id $AWS_INSTANCE_ID | The ID of the EC2 instance to image (e.g., i-1234567890abcdef0) | Yes |
| --name $AWS_AMI_NAME | Name for the new AMI (e.g., "live-compromise-ami") | Yes |
| --description $AWS_AMI_DESCRIPTION | Descriptive text for the AMI (e.g., "Live snapshot without downtime") | Yes |
| --no-reboot | Flag to skip instance reboot, enabling dirty snapshot | Yes |

## Examples

### Basic Usage

```bash
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "no-reboot-ami" --description "Stealth snapshot" --no-reboot
```

### Advanced Usage

```bash
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "persistent-ami-no-downtime" --description "Includes running malware" --no-reboot --tag-specifications 'ResourceType=image,Tags=[{Key=Stealth,Value=true}]'
```

## Expected Output

```
{
    "ImageId": "ami-0fedcba9876543210",
    "RequestId": "req-87654321-09ba-fedc-4321-0987654321ba"
}
```

The output returns the AMI ID immediately, with the instance continuing to run. Check AMI state periodically for 'available' status.

## Related

- [[procedures/AWS-Create-EC2-AMI-Image]]
- [[commands/aws-ec2-create-image]]
