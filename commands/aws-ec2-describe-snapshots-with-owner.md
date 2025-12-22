---
type: command
executor: bash
data: >-
  aws ec2 describe-snapshots --owner-id $_ACCOUNT_ID --profile $_PROFILE
  --region $_REGION
tags:
  - aws
  - ec2
  - discovery
platforms:
  - AWS
verified: true
validated: true
---

# aws-ec2-describe-snapshots-with-owner

## Command

```bash
aws ec2 describe-snapshots --owner-id $_ACCOUNT_ID --profile $_PROFILE --region $_REGION
```

## Description

Lists EBS snapshots owned by a specific AWS account ID, enabling discovery across accounts if permissions allow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --owner-id $_ACCOUNT_ID | AWS account ID (e.g., 123456789012) | Yes |
| --profile $_PROFILE | AWS CLI profile name | No |
| --region $_REGION | AWS region | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-snapshots --owner-id 123456789012
```

### Advanced Usage

With region:

```bash
aws ec2 describe-snapshots --owner-id 123456789012 --region us-west-2 --profile flaws
```

## Expected Output

JSON with snapshot details:

```json
{
  "Snapshots": [
    {
      "SnapshotId": "snap-0123456789abcdef0",
      "OwnerId": "123456789012",
      "Description": "Volume backup"
    }
  ]
}
```

## Related

- [[commands/aws-ec2-describe-snapshots]]
- [[procedures/AWS-Extract-EBS-Backup-to-EC2-Instance]]
