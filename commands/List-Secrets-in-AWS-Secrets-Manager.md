---
type: command
executor: bash
data: aws secretsmanager list-secrets
output: null
created_at: '2023-04-06T03:56:12.278295+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - aws
  - secrets-manager
verified: true
validated: true
---

# List-Secrets-in-AWS-Secrets-Manager

## Command

```bash
aws secretsmanager list-secrets
```

## Description

This command lists all secrets stored in AWS Secrets Manager for the authenticated account and region. It returns metadata about each secret, such as ARN, name, description, and last rotation date, but does not retrieve the secret values themselves. Use this during post-compromise enumeration to identify credential stores for further access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region to query (e.g., us-east-1). Defaults to AWS_DEFAULT_REGION. | No |
| `--profile` | AWS profile name from credentials file to use. | No |
| `--max-items` | Maximum number of secrets to return (default 100). | No |
| `--next-token` | Token for pagination if more than 100 secrets exist. | No |

## Examples

### Basic Usage

```bash
aws secretsmanager list-secrets
```

### With Specific Region

```bash
aws secretsmanager list-secrets --region us-west-2
```

### Paginated Query

If the response includes a NextToken, use:

```bash
aws secretsmanager list-secrets --next-token eyJvcmRlckJ5IjoiY3JlYXRlZEF0LWRlc2NlbmRpbmcifQ==
```

## Expected Output

Successful execution returns a JSON object with a SecretList array:

```json
{
    "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:MySecret-abc123",
    "Name": "MySecret",
    "Description": "Database credentials",
    "CreatedDate": "2023-01-01T12:00:00+00:00",
    "LastRotatedDate": null,
    "LastAccessedDate": "2023-09-01T10:00:00+00:00",
    "LastChangedDate": "2023-01-01T12:00:00+00:00",
    "DeletedDate": null,
    "Tags": [],
    "SecretVersionsToStages": {
        "MySecretVersion": [
            "AWSCURRENT"
        ]
    },
    "KmsKeyId": null,
    "RotationEnabled": false,
    "RotationLambdaARN": null,
    "RotationRules": null,
    "RecoverableTime": 1654041600.0
}
```

If no secrets exist or access is denied, it returns an empty list or an AccessDeniedException error.
