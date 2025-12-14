---
data: aws docdb-elastic list-cluster-snapshots
tags:
  - aws
  - docdb
  - logging
type: command
executor: bash
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
id: 68c10c57-fc4f-424d-a7b9-3579ea618236
created_at: '2025-12-14T17:32:29.149Z'
updated_at: '2025-12-14T17:32:29.149Z'
verified: false
validated: true
submitted: true
---
# aws-docdb-elastic-list-cluster-snapshots-production

## Command

```bash
aws docdb-elastic list-cluster-snapshots
```

## Description

Lists cluster snapshots for the AWS DocumentDB Elastic service using the default production endpoint. This command demonstrates standard IAM-authorized API behavior that generates CloudTrail logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None specific | Uses default region and endpoint | No |

## Examples

### Basic Usage

```bash
aws docdb-elastic list-cluster-snapshots
```

### With Region

```bash
aws docdb-elastic list-cluster-snapshots --region us-east-1
```

## Expected Output

JSON array of snapshot objects if permitted, e.g., {"clusterSnapshots": [{"snapshotName": "example"}]}; AccessDenied if not. CloudTrail log generated within 5-10 minutes.

## Related

- [[commands/aws-docdb-elastic-list-cluster-snapshots-non-production]]
- [[procedures/Demonstrate-Production-Endpoint-Logging]]
