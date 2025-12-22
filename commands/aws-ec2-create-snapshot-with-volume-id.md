---
id: 4e8b43a3-32a4-4b8f-b11e-b93c15f5d654
name: aws-ec2-create-snapshot-with-volume-id
type: command
executor: bash
data: |
  aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID
output: null
created_at: '2020-07-31T04:25:23.794742+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
  - AWS
tags:
  - AWS
  - cloud
  - snapshot
verified: true
validated: true
---

# aws-ec2-create-snapshot-with-volume-id

## Command

```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID
```

## Description

This command creates a point-in-time snapshot of the specified EBS volume using the AWS CLI. It is used in cloud post-exploitation to capture volume data for later analysis or exfiltration. The snapshot is stored durably and can be used to create new volumes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --volume-id | The ID of the EBS volume to snapshot (e.g., vol-0123456789abcdef0) | Yes |
| $AWS_VOLUME_ID | Placeholder for the volume ID, set via environment variable or direct substitution | Yes |

## Examples

### Basic Usage

```bash
aws ec2 create-snapshot --volume-id vol-0123456789abcdef0
```

### Advanced Usage

```bash
AWS_REGION=us-east-1 aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --tag-specifications 'ResourceType=snapshot,Tags=[{Key=Name,Value=CompromisedBackup}]'
```

## Expected Output

Successful execution returns JSON with snapshot details:

```json
{
    "Description": "",
    "Encrypted": false,
    "OwnerId": "123456789012",
    "Progress": "",
    "SnapshotId": "snap-066877671789bd71b",
    "StartTime": "2023-05-29T16:48:53.000Z",
    "State": "pending",
    "VolumeId": "vol-0123456789abcdef0",
    "VolumeSize": 8
}
```
Monitor with describe-snapshots until State is "completed".

## Related

- [[procedures/Create-EBS-Volume-Snapshots-for-Data-Exfiltration]]
- [[commands/aws-ec2-create-snapshot-with-volume-id-and-description]]
