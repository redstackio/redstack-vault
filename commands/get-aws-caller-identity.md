---
id: 6a8cb9a5-1ca9-4d3d-92c7-28f49c6f1aa6
name: get-aws-caller-identity
type: command
executor: bash
data: aws sts get-caller-identity
output: null
created_at: '2023-04-06T03:56:13.552770+00:00'
updated_at: '2023-04-10T20:20:54.468226+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - discovery
  - identity
verified: true
validated: true
---

# get-aws-caller-identity

## Command

```bash
aws sts get-caller-identity
```

## Description

This command queries the AWS Security Token Service to return metadata about the IAM identity and AWS account associated with the current credentials. It is a low-risk discovery action used to verify access during security testing without modifying resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | The command accepts optional flags like --output json (default) or --region us-east-1, but none are required for basic use. | No |

## Examples

### Basic Usage

```bash
aws sts get-caller-identity
```

### With Output Formatting

```bash
aws sts get-caller-identity --output table
```

## Expected Output

A JSON response detailing the identity:

```json
{
    "UserId": "AIDAJQABLZS4A3QDU576Q",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/security-auditor"
}
```

Success is indicated by a 200 OK response with the JSON object. Common errors include InvalidClientTokenId (bad credentials) or AccessDenied (policy restriction).

## Related

- [[procedures/AWS-Account-Identity-Check]]
