---
id: a3fb1f99-a51d-4052-abc1-2ba8b4e9dedf
name: aws-ec2-create-snapshot-with-volume-id-and-description
type: command
executor: bash
data: >
  aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --description
  $AWS_DESCRIPTION
output: null
created_at: '2020-07-31T04:25:23.794896+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Cloud
  - AWS
tags:
  - AWS
  - cloud
  - snapshot
  - evasion
verified: true
validated: true
---

# aws-ec2-create-snapshot-with-volume-id-and-description

## Command

```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --description $AWS_DESCRIPTION
```

## Description

This command creates an EBS snapshot with a custom description, useful for adding misleading metadata (e.g., backdated timestamps) to evade detection during forensic reviews. It builds on the basic snapshot creation by including descriptive text.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --volume-id | The ID of the EBS volume to snapshot | Yes |
| --description | A string describing the snapshot (e.g., "Backup from 2023-01-01") | No (but recommended for evasion) |
| $AWS_VOLUME_ID | Placeholder for volume ID | Yes |
| $AWS_DESCRIPTION | Placeholder for description text | Yes for this variant |

## Examples

### Basic Usage

```bash
aws ec2 create-snapshot --volume-id vol-0123456789abcdef0 --description "Automated backup"
```

### Advanced Usage (Backdating)

```bash
aws ec2 create-snapshot --volume-id $AWS_VOLUME_ID --description "snapshot-$(date -d '30 days ago' +'%Y-%m-%d_%H-%M-%S')"
```

## Expected Output

Similar to basic snapshot, with Description included:

```json
{
    "Description": "snapshot-2023-04-29_16-48-53",
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
The actual StartTime reveals true creation time; use CloudTrail for full audit.

## Related

- [[procedures/Create-EBS-Volume-Snapshots-for-Data-Exfiltration]]
- [[commands/aws-ec2-create-snapshot-with-volume-id]]
