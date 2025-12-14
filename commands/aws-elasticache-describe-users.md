---
data: aws elasticache describe-users
tags:
  - aws
  - elasticache
type: command
output: JSON response with user details; generates CloudTrail log
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.925Z'
id: 902d362b-cfee-41d9-8a96-7efa087f75ea
verified: false
validated: true
submitted: true
---
# aws-elasticache-describe-users

## Command

```bash
aws elasticache describe-users
```

## Description

Describes all ElastiCache users associated with the AWS account using the production endpoint, triggering CloudTrail logging for detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard API call without flags | No |

## Examples

### Basic Usage

```bash
aws elasticache describe-users
```

### With Region

```bash
aws elasticache describe-users --region us-east-1
```

## Expected Output

JSON array of users: {"Users": [{"ARN": "arn:aws:elasticache:...", "UserId": "user1", ...}]} or AccessDenied if unauthorized.

## Related

- [[commands/aws-elasticache-describe-users-nonprod]]
- [[procedures/Verify-Production-ElastiCache-Endpoint-Logging]]
