---
id: b873b871-ffd7-49fe-8e14-5fdd98a63204
type: command
executor: bash
data: 'aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...]]'
output: null
created_at: '2025-12-11T06:10:15.725Z'
updated_at: '2025-12-11T06:10:15.725Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - aws
  - cognito
  - verification
verified: false
validated: true
submitted: true
---

# aws-cognito-get-user-post-update

## Command

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...]]
```

## Description

Retrieves the user attributes after an update to confirm changes and verification status in AWS Cognito.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (us-east-1) | Yes |
| `--access-token` | The Cognito access token for authentication | Yes |

## Examples

### Basic Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...]]
```

### Advanced Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQi[...]] --output table
```

## Expected Output

JSON object with updated UserAttributes, showing email_verified=false and new email.

## Related

- [[commands/aws-cognito-update-user-attributes]]
- [[procedures/Verify-Email-Change]]
