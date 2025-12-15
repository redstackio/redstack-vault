---
id: cmd-prod-001
data: aws devicefarm get-account-settings --region us-west-2
tags:
  - aws
  - devicefarm
  - logging
type: command
output: JSON with account settings; CloudTrail log generated
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.639Z'
verified: false
validated: true
submitted: true
---
# aws-devicefarm-get-account-settings-production

## Command

```bash
aws devicefarm get-account-settings --region us-west-2
```

## Description

Retrieves AWS Device Farm account settings using the production endpoint, demonstrating standard CloudTrail logging for API calls with sufficient IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (e.g., us-west-2) | Yes |

## Examples

### Basic Usage

```bash
aws devicefarm get-account-settings --region us-west-2
```

### With Output Formatting

```bash
aws devicefarm get-account-settings --region us-west-2 --output json
```

## Expected Output

JSON response like: {"accountSettings": {"defaultJobTimeoutMinutes": 150, "maxJobTimeoutMinutes": 1440, "trialMinutes": {"remaining": 250}}}. Generates a CloudTrail event within 5-10 minutes.

## Related

- [[commands/aws-devicefarm-get-account-settings-non-production]]
- [[procedures/Verify-Normal-CloudTrail-Logging-with-Production-Endpoint]]
