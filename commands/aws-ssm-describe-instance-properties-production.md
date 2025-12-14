---
id: cmd-uuid-002
data: aws ssm describe-instance-properties --region us-west-2
tags:
  - aws
  - ssm
  - logging
type: command
output: API response; CloudTrail log entry after delay
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.860Z'
verified: false
validated: true
submitted: true
---
# aws-ssm-describe-instance-properties-production

## Command

```bash
aws ssm describe-instance-properties --region us-west-2
```

## Description

Calls the AWS SSM DescribeInstanceProperties API on production endpoints to describe EC2 instance properties, generating a CloudTrail log for baseline verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region | AWS region (us-west-2) | Yes |

## Examples

### Basic Usage

```bash
aws ssm describe-instance-properties --region us-west-2
```

### Advanced Usage

```bash
aws ssm describe-instance-properties --region us-west-2 --instance-id i-1234567890abcdef0
```

## Expected Output

JSON array of instance properties; CloudTrail event logged within 5-10 minutes.

## Related

- [[commands/aws-ssm-describe-instance-properties-nonprod]]
- [[procedures/Demonstrate-Normal-CloudTrail-Logging-with-SSM-API]]
