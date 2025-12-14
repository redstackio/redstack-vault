---
id: cmd-001
data: >-
  aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...]
  (redacted token)
tags:
  - cognito
  - recon
type: command
output: >-
  JSON with Username and UserAttributes array including sub, birthdate,
  email_verified, locale, given_name, family_name, email
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.435Z'
verified: false
validated: true
submitted: true
---
# aws-cognito-get-user

## Command

```bash
aws cognito-idp get-user --region us-east-1 --access-token eyJraWQiOiJPVj[...] (redacted token)
```

## Description

Retrieves the current user's attributes from AWS Cognito User Pool using a bearer access token. Used to inspect email, verification status, and other details before or after modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region for the Cognito pool (e.g., us-east-1) | Yes |
| `--access-token` | Bearer token obtained from authentication | Yes |

## Examples

### Basic Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token <token>
```

### Advanced Usage

```bash
aws cognito-idp get-user --region us-east-1 --access-token <token> --output json
```

## Expected Output

JSON object with "Username" and "UserAttributes" array, e.g., {"UserAttributes": [{"Name": "email", "Value": "attacker@example.com"}, {"Name": "email_verified", "Value": "true"}]}. After update, email_verified may be "false".

## Related

- [[commands/aws-cognito-update-user-attributes]]
- [[procedures/Retrieve-Cognito-User-Attributes]]
