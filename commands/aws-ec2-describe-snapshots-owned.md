---
id: 8ee218b0-c3d0-49ac-8880-851e70249d3f
name: aws-ec2-describe-snapshots-owned
type: command
executor: bash
data: aws ec2 describe-snapshots --owner-ids self
output: null
created_at: '2023-04-06T03:56:13.725649+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - cloud
  - ebs
verified: true
validated: true
---

# aws-ec2-describe-snapshots-owned

## Command

```bash
aws ec2 describe-snapshots --owner-ids self
```

## Description

This AWS CLI command queries the EC2 API to retrieve details about all EBS snapshots owned by the authenticated AWS account. It is used in cloud enumeration to identify backup data for potential exfiltration or manipulation, focusing only on account-specific snapshots to avoid public noise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--owner-ids` | Filters snapshots by owner; `self` limits to the current account | Yes |
| `self` | Specifies the authenticated account as the owner | Yes (with --owner-ids) |

## Examples

### Basic Usage

```bash
aws ec2 describe-snapshots --owner-ids self
```

### Advanced Usage (with output formatting)

```bash
aws ec2 describe-snapshots --owner-ids self --query 'Snapshots[*].[SnapshotId,Description,State]' --output table
```

## Expected Output

Successful execution returns a JSON object with a `Snapshots` array containing details like:

```json
{
    "Snapshots": [
        {
            "Description": "Backup of prod volume",
            "Encrypted": true,
            "OwnerId": "123456789012",
            "Progress": "100%",
            "SnapshotId": "snap-0123456789abcdef0",
            "StartTime": "2023-09-01T12:00:00.000Z",
            "State": "completed",
            "VolumeId": "vol-0123456789abcdef0",
            "VolumeSize": 8
        }
    ]
}
```

If no snapshots exist, `Snapshots` is an empty array. Errors include `UnauthorizedOperation` for insufficient permissions.

## Related

- [[procedures/Enumerate-AWS-EBS-Snapshots]] (procedure that uses this command)
- [[tools/AWS-CLI]] (tool required)
