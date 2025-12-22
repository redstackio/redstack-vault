---
type: command
executor: bash
data: >-
  aws ec2 create-image --instance-id $_INSTANCE_ID --name "$_IMAGE_NAME"
  --description "$_DESCRIPTION" --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - ami
  - persistence
verified: true
validated: true
---

# aws-ec2-create-image-from-instance

## Command

```bash
aws ec2 create-image --instance-id $_INSTANCE_ID --name "$_IMAGE_NAME" --description "$_DESCRIPTION" --region $_REGION
```

## Description

Creates an AMI from a running or stopped EC2 instance, capturing its configuration for duplication. Useful for backing up or cloning compromised instances in offensive operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INSTANCE_ID | ID of the source instance (e.g., i-0438b003d81cd7ec5) | Yes |
| $_IMAGE_NAME | Name for the new AMI (e.g., "Cloned Instance") | Yes |
| $_DESCRIPTION | Description of the AMI | Yes |
| $_REGION | AWS region | Yes |
| --no-reboot | Create without rebooting (less consistent) | No |

## Examples

### Basic Usage

```bash
aws ec2 create-image --instance-id i-0438b003d81cd7ec5 --name "AWS Audit" --description "Export AMI" --region eu-west-1
```

### With No Reboot

```bash
aws ec2 create-image --instance-id i-123456 --name "Live Clone" --description "Cloned live" --no-reboot --region us-east-1
```

## Expected Output

JSON with new AMI ID:
```
{
    "ImageId": "ami-0abcdef1234567890"
}
```
Success: AMI ID returned; monitor status with describe-images.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-describe-images-by-region]]
