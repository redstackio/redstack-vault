---
id: 81b86f2b-9ae9-4d0d-a4c5-b92cda5212ba
type: command
executor: bash
data: >-
  aws cognito-idp get-user --region us-east-1 --access-token
  eyJraWQiOiJPVj[...]]
output: null
created_at: '2025-12-11T06:10:15.732Z'
updated_at: '2025-12-11T06:10:15.732Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - aws
  - cognito
  - discovery
verified: false
validated: true
submitted: true
---

# aws-cognito-get-user

## Command

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]]
```

## Description

Retrieves the user attributes for the authenticated user in AWS Cognito, used to view current details like email before changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (us-east-1) | Yes |
| `--access-token` | The Cognito access token for authentication | Yes |

## Examples

### Basic Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]]
```

### Advanced Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]] --output json
```

## Expected Output

JSON object with Username and UserAttributes including sub, birthdate, email_verified, locale, given_name, family_name, email.

## Related

- [[commands/aws-cognito-update-user-attributes]]
- [[procedures/Retrieve-User-Details-via-AWS-CLI]]
