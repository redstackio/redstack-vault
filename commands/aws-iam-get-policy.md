---
id: edf3a891-1906-4f46-baa8-74adaeaab3c3
name: AWS IAM Get Policy
type: command
executor: bash
data: aws iam get-policy --policy-arn $_POLICY_ARN
output: null
created_at: '2023-04-06T03:56:10.288692+00:00'
updated_at: '2023-04-10T20:20:14.072280+00:00'
platforms:
  - AWS
tags:
  - cloud
  - discovery
  - iam
verified: true
validated: true
---

# AWS IAM Get Policy

## Command

```bash
aws iam get-policy --policy-arn $_POLICY_ARN
```

## Description

This command retrieves metadata for a specific IAM policy using its ARN. It is used during cloud discovery to gather policy details like name, description, attachment count, and default version without fetching the full permissions document. Requires iam:GetPolicy permission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --policy-arn $_POLICY_ARN | The Amazon Resource Name (ARN) of the IAM policy (e.g., arn:aws:iam::123456789012:policy/MyPolicy) | Yes |

## Examples

### Basic Usage

```bash
aws iam get-policy --policy-arn arn:aws:iam::123456789012:policy/MyPolicy
```

### With Output Formatting

```bash
aws iam get-policy --policy-arn arn:aws:iam::123456789012:policy/MyPolicy --output table
```

## Expected Output

Successful execution returns JSON metadata about the policy:

```json
{
    "Policy": {
        "PolicyName": "MyPolicy",
        "PolicyId": "ANPAJKWEXAMPLE",
        "Arn": "arn:aws:iam::123456789012:policy/MyPolicy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 1,
        "IsAttachable": true,
        "Description": "Sample policy",
        "CreateDate": "2015-03-09T18:43:32.752Z"
    }
}
```

Error if policy not found or insufficient permissions: "An error occurred (NoSuchEntity) when calling the GetPolicy operation"

## Related

- [[procedures/AWS-IAM-Policy-Information-Retrieval]]
- [[commands/aws-iam-get-policy-version]]
