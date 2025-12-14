---
id: cmd-uuid-003
data: aws ssm describe-instance-properties --region us-west-2 --endpoint-url ██████
tags:
  - aws
  - ssm
  - evasion
type: command
output: >-
  API response (success or AccessDeniedException based on permissions); no
  CloudTrail log
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.858Z'
verified: false
validated: true
submitted: true
---
# aws-ssm-describe-instance-properties-nonprod

## Command

```bash
aws ssm describe-instance-properties --region us-west-2 --endpoint-url ██████
```

## Description

Executes SSM DescribeInstanceProperties on a non-production endpoint (redacted ██████), bypassing CloudTrail logging for silent permission enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region | AWS region (us-west-2) | Yes |
| --endpoint-url | Non-production URL (█████) | Yes |

## Examples

### Basic Usage

```bash
aws ssm describe-instance-properties --region us-west-2 --endpoint-url ██████
```

### Advanced Usage

```bash
aws ssm describe-instance-properties --region us-west-2 --endpoint-url ██████ --instance-id i-1234567890abcdef0
```

## Expected Output

Success JSON or AccessDeniedException; no log in CloudTrail.

## Related

- [[commands/aws-ssm-describe-instance-properties-production]]
- [[procedures/Execute-SSM-API-on-Non-Production-Endpoint]]
