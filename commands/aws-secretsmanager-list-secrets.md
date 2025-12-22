---
id: 8aca45ac-0f82-4377-a149-9b85bed495bf
name: aws-secretsmanager-list-secrets
type: command
executor: bash
data: aws secretsmanager list-secrets
output: null
created_at: '2023-04-06T03:56:12.077663+00:00'
updated_at: '2023-04-10T20:20:52.332197+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - cloud-aws
  - enumeration
verified: true
validated: true
---

# aws-secretsmanager-list-secrets

## Command

```bash
aws secretsmanager list-secrets
```

## Description

This command lists all secrets stored in the AWS Secrets Manager for the authenticated account and region. It is used during cloud discovery to identify sensitive credentials and configurations without retrieving their values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` (or `AWS_REGION` env) | AWS region to query (e.g., us-east-1) | No (defaults to configured region) |
| `--profile` (or `AWS_PROFILE` env) | AWS profile name for credentials | No (defaults to default profile) |
| `--output` | Output format (json, text, table) | No (defaults to json) |
| `--query` | JMESPath query to filter output | No |
| `--max-items` | Maximum number of secrets to return | No |
| `--next-token` | Token for paginated results | No |

## Examples

### Basic Usage

```bash
aws secretsmanager list-secrets
```

### Advanced Usage

```bash
aws secretsmanager list-secrets --region us-west-2 --output table --query 'SecretList[*].{Name:Name,ARN:ARN}'
```

## Expected Output

A JSON object with a `SecretList` array detailing each secret's metadata. For example:

```json
{
    "SecretList": [
        {
            "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:example-secret-XYZ",
            "Name": "example-secret",
            "Description": "Example secret for testing",
            "CreatedDate": "2023-01-01T00:00:00Z"
        }
    ]
}
```

If no secrets exist, `SecretList` is an empty array. Errors like `AccessDeniedException` indicate insufficient permissions.

## Related

- [[procedures/Enumerate-AWS-Secrets-Manager-Secrets]]
