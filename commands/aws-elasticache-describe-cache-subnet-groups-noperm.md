---
data: aws elasticache describe-cache-subnet-groups --endpoint-url ███
tags:
  - aws
  - elasticache
  - access-denied
type: command
output: AccessDenied error message
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.912Z'
id: dbe1ab80-aa3d-4c9f-93f2-cf88eb0b3281
verified: false
validated: true
submitted: true
---
# aws-elasticache-describe-cache-subnet-groups-noperm

## Command

```bash
aws elasticache describe-cache-subnet-groups --endpoint-url ███
```

## Description

Tests describe-cache-subnet-groups on non-production endpoint with non-privileged profile, resulting in AccessDenied without logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url | Non-production URL (███) | Yes |

## Examples

### Basic Usage

```bash
aws elasticache describe-cache-subnet-groups --endpoint-url ███
```

## Expected Output

Error: An error occurred (AccessDenied) when calling the DescribeCacheSubnetGroups operation: User: arn:aws:sts::111111111111:assumed-role/noperm/noperm is not authorized...

## Related

- [[commands/aws-elasticache-describe-cache-subnet-groups-admin]]
- [[procedures/Enumerate-IAM-Permissions-with-Non-Production-Endpoint]]
