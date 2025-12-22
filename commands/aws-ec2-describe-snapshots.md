---
type: command
executor: bash
data: >-
  aws ec2 describe-snapshots --owner-ids self --profile $_PROFILE --region
  $_REGION
tags:
  - aws
  - ec2
  - discovery
platforms:
  - AWS
verified: true
validated: true
---

# aws-ec2-describe-snapshots

## Command

```bash
aws ec2 describe-snapshots --owner-ids self --profile $_PROFILE --region $_REGION
```

## Description

Retrieves details of EBS snapshots owned by the current account, useful for discovering available backups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --owner-ids self | Limits to snapshots owned by the caller | Yes |
| --profile $_PROFILE | AWS CLI profile name | No |
| --region $_REGION | AWS region | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-snapshots --owner-ids self
```

### Advanced Usage

With filters:

```bash
aws ec2 describe-snapshots --owner-ids self --filters "Name=description,Values=*backup*" --region us-west-2
```

## Expected Output

JSON array of snapshots:

```json
{
  "Snapshots": [
    {
      "SnapshotId": "snap-0123456789abcdef0",
      "Description": "Backup of /dev/xvda",
      "Encrypted": false,
      "VolumeId": "vol-049df6151d250842f"
    }
  ]
}
```

## Related

- [[commands/aws-ec2-describe-snapshots-with-owner]]
- [[procedures/AWS-Extract-EBS-Backup-to-EC2-Instance]]
