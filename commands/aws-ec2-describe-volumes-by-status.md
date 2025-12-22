---
id: e8e83274-20f1-416f-9714-60754e29e008
name: aws-ec2-describe-volumes-by-status
type: command
executor: bash
data: >
  aws ec2 describe-volumes --filters
  "Name=status,Values=available,in-use,optimizing,error"
output: null
created_at: '2020-07-31T04:25:29.577537+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - AWS
tags:
  - Discovery
  - AWS
verified: true
validated: true
---

# aws-ec2-describe-volumes-by-status

## Command

```bash
aws ec2 describe-volumes --filters "Name=status,Values=available,in-use,optimizing,error"
```

## Description

This command lists EBS volumes filtered by their status (e.g., available for unused, in-use for attached). It helps isolate potentially mountable volumes during discovery, focusing on states that indicate low-risk access or errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --filters | Filter by name-value pairs (e.g., Name=status,Values=available,in-use) | Yes |
| --region | Specify AWS region | No |
| --output | Output format | No |

## Examples

### Basic Filtered Usage

```bash
aws ec2 describe-volumes --filters "Name=status,Values=available,in-use"
```

### Include Error States

```bash
aws ec2 describe-volumes --filters "Name=status,Values=available,in-use,optimizing,error" --output table
```

## Expected Output

```
{
    "Volumes": [
        {
            "VolumeId": "vol-1234567890abcdef0",
            "State": "available",
            "Size": 8,
            "Attachments": []
        },
        {
            "VolumeId": "vol-0987654321fedcba0",
            "State": "in-use",
            "Attachments": [{"InstanceId": "i-1234567890abcdef0"}]
        }
    ]
}
```
Filtered JSON showing only volumes in specified states. Available volumes without attachments are prime for mounting.

## Related

- [[Related Procedure: Enumerate-AWS-EBS-Volumes]]
- [[Related Command: aws-ec2-describe-all-volumes]]
