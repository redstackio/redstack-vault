---
data: aws docdb-elastic list-cluster-snapshots --endpoint-url ██████
tags:
  - aws
  - docdb
  - bypass
type: command
executor: bash
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
id: f20c1ee6-484f-48d2-a98e-918c87081fd2
created_at: '2025-12-14T17:32:29.147Z'
updated_at: '2025-12-14T17:32:29.147Z'
verified: false
validated: true
submitted: true
---
# aws-docdb-elastic-list-cluster-snapshots-non-production

## Command

```bash
aws docdb-elastic list-cluster-snapshots --endpoint-url ██████
```

## Description

Lists cluster snapshots for AWS DocumentDB Elastic but targets a non-production endpoint via --endpoint-url override, bypassing CloudTrail logging while applying IAM checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--endpoint-url` | Custom URL for non-production endpoint (redacted as ██████) | Yes |

## Examples

### Basic Usage

```bash
aws docdb-elastic list-cluster-snapshots --endpoint-url ██████
```

### With Additional Flags

```bash
aws docdb-elastic list-cluster-snapshots --endpoint-url ██████ --region us-east-1
```

## Expected Output

JSON response similar to production (success or AccessDenied); no CloudTrail log after 5-10 minutes.

## Related

- [[commands/aws-docdb-elastic-list-cluster-snapshots-production]]
- [[procedures/Invoke-Non-Production-Endpoint]]
