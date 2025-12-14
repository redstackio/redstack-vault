---
id: cmd-uuid-1
data: aws forecast list-datasets --region us-west-2
tags:
  - aws
  - forecast
type: command
output: null
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.602Z'
verified: false
validated: true
submitted: true
---
# aws-forecast-list-datasets-production

## Command

```bash
aws forecast list-datasets --region us-west-2
```

## Description

Lists datasets in the AWS Forecast service using the production endpoint, demonstrating standard logging to CloudTrail. Use with IAM credentials to test access and verify audit trails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (e.g., us-west-2) | Yes |

## Examples

### Basic Usage

```bash
aws forecast list-datasets --region us-west-2
```

### With Output to File

```bash
aws forecast list-datasets --region us-west-2 --output json > datasets.json
```

## Expected Output

JSON array of dataset objects if permitted, e.g., {"Datasets": [{"DatasetArn": "..."}]}; AccessDeniedError if not. CloudTrail log generated within 5-10 minutes.

## Related

- [[commands/aws-forecast-list-datasets-nonprod]]
- [[procedures/Test-Production-Forecast-Endpoint-Logging]]
