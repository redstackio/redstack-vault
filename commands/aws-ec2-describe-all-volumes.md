---
id: eefc7864-7916-4984-bfd1-4750b5efccc7
name: aws-ec2-describe-all-volumes
type: command
executor: bash
data: |
  aws ec2 describe-volumes
output: null
created_at: '2020-07-31T04:25:29.577452+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - AWS
tags:
  - Discovery
  - AWS
verified: true
validated: true
---

# aws-ec2-describe-all-volumes

## Command

```bash
aws ec2 describe-volumes
```

## Description

This command retrieves detailed information about all Elastic Block Store (EBS) volumes in the specified AWS region, including volume IDs, sizes, states, and attachments. Use it during cloud reconnaissance to identify storage resources and potential data sources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None (default) | Lists all volumes without filters | No |
| --region | Specify AWS region (e.g., us-east-1) | No |
| --output | Format output (json, table, text) | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-volumes
```

### With Region and JSON Output

```bash
aws ec2 describe-volumes --region us-west-2 --output json
```

## Expected Output

```
{
    "Volumes": [
        {
            "AvailabilityZone": "us-east-1a",
            "VolumeId": "vol-1234567890abcdef0",
            "State": "available",
            "Size": 8,
            "Attachments": [],
            "VolumeType": "gp2",
            "Iops": 100
        }
    ]
}
```
A JSON array of volume objects. Look for 'State': 'available' and empty 'Attachments' to identify unused volumes.

## Related

- [[Related Procedure: Enumerate-AWS-EBS-Volumes]]
- [[Related Command: aws-ec2-describe-volumes-by-status]]
