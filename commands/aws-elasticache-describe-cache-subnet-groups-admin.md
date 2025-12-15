---
data: aws elasticache describe-cache-subnet-groups --endpoint-url ████████
tags:
  - aws
  - elasticache
  - permission-enumeration
type: command
output: '{"CacheSubnetGroups": []}'
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.918Z'
id: e2c573e1-8ea1-4a17-9e1b-1f3d942de054
verified: false
validated: true
submitted: true
---
# aws-elasticache-describe-cache-subnet-groups-admin

## Command

```bash
aws elasticache describe-cache-subnet-groups --endpoint-url ████████
```

## Description

Describes cache subnet groups via non-production endpoint with admin profile, succeeding without logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url | Non-production URL (████████) | Yes |

## Examples

### Basic Usage

```bash
aws elasticache describe-cache-subnet-groups --endpoint-url ████████
```

## Expected Output

{"CacheSubnetGroups": []} for empty successful response.

## Related

- [[commands/aws-elasticache-describe-cache-subnet-groups-noperm]]
- [[procedures/Enumerate-IAM-Permissions-with-Non-Production-Endpoint]]
