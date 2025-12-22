---
id: 4166847f-ae4d-4763-b4b8-aa49f8f35222
name: aws-ec2-create-snapshot
type: command
executor: bash
data: >-
  aws ec2 create-snapshot --volume-id $_VOLUME_ID --description
  "$_SNAPSHOT_DESCRIPTION" --profile $_PROFILE_NAME --region $_REGION
output: null
created_at: '2023-04-06T03:56:13.750800+00:00'
updated_at: '2023-04-10T20:20:36.202580+00:00'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - snapshot
  - ebs
verified: true
validated: true
---

# aws-ec2-create-snapshot

## Command

```bash
aws ec2 create-snapshot --volume-id $_VOLUME_ID --description "$_SNAPSHOT_DESCRIPTION" --profile $_PROFILE_NAME --region $_REGION
```

## Description

This command creates an EBS snapshot of the specified volume using the AWS CLI. It captures the volume's data at a point in time, storing it durably in S3. Useful for backups or, in attack scenarios, data exfiltration from compromised AWS environments. Requires 'ec2:CreateSnapshot' permission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --volume-id $_VOLUME_ID | The ID of the EBS volume to snapshot (e.g., vol-0123456789abcdef0) | Yes |
| --description "$_SNAPSHOT_DESCRIPTION" | Optional description for the snapshot (e.g., "Data backup") | No |
| --profile $_PROFILE_NAME | Name of the AWS CLI profile with credentials (defaults to 'default' if omitted) | No |
| --region $_REGION | AWS region (e.g., us-east-1; defaults to profile's default) | No |

## Examples

### Basic Usage

```bash
aws ec2 create-snapshot --volume-id vol-0123456789abcdef0 --description "Exfil snapshot"
```

### Advanced Usage

```bash
aws ec2 create-snapshot --volume-id vol-0123456789abcdef0 --description "Sensitive data capture" --profile attacker-profile --region us-west-2
```

## Expected Output

Successful execution returns a JSON response indicating the snapshot creation:

```json
{
    "Description": "Sensitive data capture",
    "Encrypted": false,
    "OwnerId": "123456789012",
    "Progress": "",
    "SnapshotId": "snap-0123456789abcdef0",
    "StartTime": "2023-04-10T20:00:00+00:00",
    "State": "pending",
    "VolumeId": "vol-0123456789abcdef0",
    "VolumeSize": 8
}
```

The 'State' will change to 'completed' after processing (monitor with describe-snapshots). Errors include 'UnauthorizedOperation' if permissions lack.

## Related

- [[procedures/Create-EBS-Snapshot-for-Data-Exfiltration]]
- [[commands/aws-ec2-describe-volumes]]
