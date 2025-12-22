---
id: 633f2ee6-ddd3-4a52-a8fb-1bad5f24a206
name: aws-sts-get-caller-identity
type: command
executor: bash
data: aws sts get-caller-identity
output: null
created_at: '2023-04-06T03:56:13.431244+00:00'
updated_at: '2023-04-10T20:20:47.805538+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - cloud
  - aws
  - discovery
verified: true
validated: true
---

# aws-sts-get-caller-identity

## Command

```bash
aws sts get-caller-identity
```

## Description

This command retrieves metadata about the AWS identity making the request, including the account ID, ARN, and user ID. It is used for initial reconnaissance in AWS environments to confirm access and map the account without requiring special permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The command has no required parameters; optional flags like --output (json/text/table) can format results. | No |

## Examples

### Basic Usage

```bash
aws sts get-caller-identity
```

Returns JSON output with identity details.

### Advanced Usage

```bash
aws sts get-caller-identity --output text --query Account
```

Extracts just the account ID in plain text for scripting.

## Expected Output

Successful execution returns JSON like:

```json
{
    "UserId": "AIDAXYZ1234567890",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/testuser"
}
```

This confirms the calling identity and account scope.

## Related

- [[procedures/AWS-Account-Identity-Enumeration]]
- [[tools/aws-cli]]
