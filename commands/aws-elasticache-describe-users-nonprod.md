---
data: aws elasticache describe-users --endpoint-url ███████
tags:
  - aws
  - elasticache
  - logging-bypass
type: command
output: JSON response or AccessDenied; no CloudTrail log
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.923Z'
id: 36e17b3b-5e9a-41da-bfc4-83717a29dbc7
verified: false
validated: true
submitted: true
---
# aws-elasticache-describe-users-nonprod

## Command

```bash
aws elasticache describe-users --endpoint-url ███████
```

## Description

Describes ElastiCache users via non-production endpoint, bypassing CloudTrail while checking IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url | Custom non-production URL (███████) | Yes |

## Examples

### Basic Usage

```bash
aws elasticache describe-users --endpoint-url ███████
```

## Expected Output

JSON with users or AccessDenied; no log generated.

## Related

- [[commands/aws-elasticache-describe-users]]
- [[procedures/Test-Non-Production-ElastiCache-Endpoint-No-Logging]]
