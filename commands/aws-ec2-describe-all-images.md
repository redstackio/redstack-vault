---
id: f0748826-36ed-4812-a168-ed99f7a382c5
name: aws-ec2-describe-all-images
type: command
executor: bash
data: |
  aws ec2 describe-images
output: null
created_at: '2020-07-31T04:25:19.326708+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
tags:
  - aws
  - ec2
  - discovery
verified: true
validated: true
---

# aws-ec2-describe-all-images

## Command

```bash
aws ec2 describe-images
```

## Description

This command lists all Amazon Machine Images (AMIs) accessible in the current AWS account and region. It is used for initial discovery of available images without any filtering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | No parameters; uses default AWS CLI configuration for profile and region. | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-images
```

### With Output Formatting

```bash
aws ec2 describe-images | jq '.Images[] | {ImageId, Name, CreationDate}'
```

## Expected Output

A JSON object containing an array of Images, each with properties like ImageId, Name, Description, Architecture (e.g., x86_64), CreationDate, and State (available).

Example snippet:
```
{
    "Images": [
        {
            "Architecture": "x86_64",
            "CreationDate": "2023-01-01T00:00:00.000Z",
            "ImageId": "ami-0abcdef1234567890",
            "Name": "My-Custom-AMI",
            "State": "available"
        }
    ]
}
```

## Related

- [[procedures/Enumerate-AWS-EC2-AMIs]]
- [[commands/aws-ec2-describe-image-by-id]]
