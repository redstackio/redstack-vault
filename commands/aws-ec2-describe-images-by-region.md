---
type: command
executor: bash
data: aws ec2 describe-images --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - ami
  - recon
verified: true
validated: true
---

# aws-ec2-describe-images-by-region

## Command

```bash
aws ec2 describe-images --region $_REGION
```

## Description

This command retrieves a list of Amazon Machine Images (AMIs) in the specified AWS region, including details like ID, name, description, and state. Use it for reconnaissance of available images before creating or launching instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REGION | AWS region (e.g., us-east-1, eu-west-1) | Yes |
| --filters | Optional filters (e.g., "Name=owner-id,Values=amazon") | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-images --region eu-west-1
```

### Filtered Usage

```bash
aws ec2 describe-images --region us-east-1 --owners self
```

## Expected Output

JSON array of AMI objects:
```
{
    "Images": [
        {
            "ImageId": "ami-0b77e2d906b00202d",
            "Name": "AWS Audit",
            "State": "available",
            "CreationDate": "2023-04-06T03:56:09.000Z"
        }
    ]
}
```
Success: Images array populated without errors.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-create-image-from-instance]]
