---
id: cmd-uuid-2
data: aws forecast list-datasets --region us-west-2 --endpoint-url ███████
tags:
  - aws
  - forecast
  - evasion
type: command
output: null
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.598Z'
verified: false
validated: true
submitted: true
---
# aws-forecast-list-datasets-nonprod

## Command

```bash
aws forecast list-datasets --region us-west-2 --endpoint-url ███████
```

## Description

Lists datasets in AWS Forecast using a non-production endpoint override, bypassing CloudTrail logging while respecting IAM permissions. Ideal for stealthy permission tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region | Yes |
| `--endpoint-url` | Custom non-production URL (redacted) | Yes |

## Examples

### Basic Usage

```bash
aws forecast list-datasets --region us-west-2 --endpoint-url ███████
```

### For Other Operations

```bash
aws forecast create-dataset --region us-west-2 --endpoint-url ███████ --cli-input-json file://input.json
```

## Expected Output

Similar to production: JSON datasets or AccessDenied; no CloudTrail log after 5-10+ minutes.

## Related

- [[commands/aws-forecast-list-datasets-production]]
- [[procedures/Test-Non-Production-Forecast-Endpoint-Logging]]
