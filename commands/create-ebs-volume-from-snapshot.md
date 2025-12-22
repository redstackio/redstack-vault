---
id: 7d8c56be-c76e-4b82-9984-7f2dc50e3c6a
name: create-ebs-volume-from-snapshot
type: command
executor: bash
data: >-
  aws ec2 create-volume --snapshot-id $_SNAPSHOT_ID --availability-zone
  $_AVAILABILITY_ZONE --volume-type $_VOLUME_TYPE --size $_SIZE_GB
output: null
created_at: '2023-04-06T03:56:09.541861+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - ebs
  - cloud
verified: true
validated: true
---

# create-ebs-volume-from-snapshot

## Command

```bash
aws ec2 create-volume --snapshot-id $_SNAPSHOT_ID --availability-zone $_AVAILABILITY_ZONE --volume-type $_VOLUME_TYPE --size $_SIZE_GB
```

## Description

This command creates a new EBS volume from an existing snapshot in the specified Availability Zone, useful for duplicating storage for analysis or attachment without altering the original.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --snapshot-id $_SNAPSHOT_ID | ID of the snapshot to base the volume on (e.g., snap-0123456789abcdef0) | Yes |
| --availability-zone $_AVAILABILITY_ZONE | AWS Availability Zone (e.g., us-east-1a) where the volume will be created | Yes |
| --volume-type $_VOLUME_TYPE | Type of volume (e.g., gp3, io2); defaults to gp2 | No |
| --size $_SIZE_GB | Size in GiB; must be at least the snapshot size | No |

## Examples

### Basic Usage

```bash
aws ec2 create-volume --snapshot-id snap-0123456789abcdef0 --availability-zone us-east-1a
```

### Advanced Usage

```bash
aws ec2 create-volume --snapshot-id snap-0123456789abcdef0 --availability-zone us-east-1a --volume-type gp3 --size 100
```

## Expected Output

{
    "AvailabilityZone": "us-east-1a",
    "CreateTime": "2023-10-01T12:00:00+00:00",
    "Encrypted": false,
    "Size": 8,
    "SnapshotId": "snap-0123456789abcdef0",
    "State": "creating",
    "VolumeId": "vol-0123456789abcdef0",
    "VolumeType": "gp2",
    "Iops": 100,
    "Tags": []
}

## Related

- [[procedures/Mount-EBS-Volume-to-EC2-Linux-Instance]]
- [[commands/attach-ebs-volume-to-ec2-instance]]
