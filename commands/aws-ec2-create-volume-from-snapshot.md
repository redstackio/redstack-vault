---
id: 67c7277d-259a-4c9f-8c24-2ec5d067e97c
name: aws-ec2-create-volume-from-snapshot
type: command
executor: bash
data: >-
  aws ec2 create-volume --snapshot-id $_SNAPSHOT_ID --availability-zone
  $_AVAILABILITY_ZONE --profile $_PROFILE_NAME
output: null
created_at: '2023-04-06T03:56:13.800483+00:00'
updated_at: '2023-04-10T20:20:10.457037+00:00'
platforms:
  - AWS
tags:
  - aws
  - ebs
  - cloud
verified: true
validated: true
---

# aws-ec2-create-volume-from-snapshot

## Command

```bash
aws ec2 create-volume --snapshot-id $_SNAPSHOT_ID --availability-zone $_AVAILABILITY_ZONE --profile $_PROFILE_NAME
```

## Description

Creates a new EBS volume from a specified snapshot in the given Availability Zone. This is the first step in restoring snapshot data for analysis or exfiltration in cloud environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SNAPSHOT_ID | ID of the source snapshot (e.g., snap-0123456789abcdef0) | Yes |
| $_AVAILABILITY_ZONE | Target Availability Zone (e.g., us-east-1a) | Yes |
| $_PROFILE_NAME | AWS CLI profile name (e.g., default) | No (uses default if omitted) |

## Examples

### Basic Usage

```bash
aws ec2 create-volume --snapshot-id snap-0123456789abcdef0 --availability-zone us-east-1a
```

### With Custom Profile

```bash
aws ec2 create-volume --snapshot-id snap-0123456789abcdef0 --availability-zone us-east-1a --profile compromised-profile
```

## Expected Output

```
{
    "AvailabilityZone": "us-east-1a",
    "CreateTime": "2023-04-06T03:56:13+00:00",
    "Encrypted": false,
    "Size": 8,
    "SnapshotId": "snap-0123456789abcdef0",
    "State": "creating",
    "VolumeId": "vol-049df61146c4d7901",
    "VolumeType": "gp2"
}
```
The VolumeId is key for attachment; poll with `describe-volumes` until State is 'available'.

## Related

- [[procedures/AWS-EBS-Snapshot-Volume-Creation]]
- [[commands/aws-ec2-attach-volume-to-instance]]
