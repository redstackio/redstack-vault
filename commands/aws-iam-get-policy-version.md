---
id: 9a4432c0-9f05-4346-83bc-fef1bd2ea283
name: aws-iam-get-policy-version
type: command
executor: bash
data: aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
output: null
created_at: '2023-04-06T03:56:10.780814+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-get-policy-version

## Command

```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

## Description

This command retrieves details about a specific version of an IAM policy, including its JSON document with permission statements. Use it during cloud discovery to analyze permissions for potential escalation paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --policy-arn $_POLICY_ARN | The ARN of the IAM policy (e.g., arn:aws:iam::123456789012:policy/MyPolicy) | Yes |
| --version-id $_VERSION_ID | The version ID of the policy (e.g., v1) | Yes |

## Examples

### Basic Usage

```bash
aws iam get-policy-version --policy-arn arn:aws:iam::123456789012:policy/ExamplePolicy --version-id v1
```

### Advanced Usage

```bash
aws iam get-policy-version --policy-arn arn:aws:iam::123456789012:policy/ExamplePolicy --version-id v2 --output json > policy.json
```

## Expected Output

```
{
    "PolicyVersion": {
        "Document": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "s3:GetObject",
                    "Effect": "Allow",
                    "Resource": "*"
                }
            ]
        },
        "VersionId": "v1",
        "IsDefaultVersion": false,
        "CreateDate": "2023-01-01T00:00:00+00:00"
    }
}
```

A successful response includes the policy document; errors occur if credentials lack permission or ARN/version is invalid.

## Related

- [[procedures/Gather-AWS-IAM-Policy-Version-Information]]
