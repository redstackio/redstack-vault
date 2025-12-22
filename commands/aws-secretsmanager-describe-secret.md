---
type: command
executor: bash
data: aws secretsmanager describe-secret --secret-id $_SECRET_ID --profile $_PROFILE
output: null
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - aws
verified: true
validated: true
---

# AWS Secrets Manager Describe Secret

## Command

```bash
aws secretsmanager describe-secret --secret-id $_SECRET_ID --profile $_PROFILE
```

## Description

This command retrieves metadata about a specific secret in AWS Secrets Manager without exposing the secret value. Use it during reconnaissance to map out secrets in the target AWS environment, identifying potential credential stores or API key holders.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --secret-id $_SECRET_ID | The unique identifier (name or ARN) of the secret to describe (e.g., 'prod-db-password' or 'arn:aws:secretsmanager:us-east-1:123456789012:secret:prod-db-password-abc123') | Yes |
| --profile $_PROFILE | AWS CLI profile name containing the credentials (omit if using default profile) | No |
| --region $_REGION | AWS region where the secret resides (e.g., 'us-east-1'; defaults to default region) | No |

## Examples

### Basic Usage

Describe a secret using its name:

```bash
aws secretsmanager describe-secret --secret-id prod-db-password
```

### Advanced Usage

Describe a secret with a specific profile and region, piping to jq for parsing:

```bash
aws secretsmanager describe-secret --secret-id prod-db-password --profile attacker-profile --region us-west-2 | jq '.Name'
```

## Expected Output

Successful execution returns a JSON object with secret metadata:

```json
{
    "ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:prod-db-password-abc123",
    "Name": "prod-db-password",
    "Description": "Password for production database",
    "KMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "RotationEnabled": false,
    "CreatedDate": "2023-01-01T12:00:00+00:00"
}
```

Look for fields like Description to infer the secret's purpose. Errors include 'AccessDenied' (403) for permission issues or 'ResourceNotFound' (404) for invalid IDs.

## Related

- [[Related Procedure]]: [[procedures/aws-secrets-manager-enumeration]]
- [[Related Command]]: [[commands/aws-secretsmanager-list-secrets]]
