---
id: 8973cafc-0f10-423a-b9dd-9aebd307cd9c
name: aws-iam-list-policy-versions
type: command
executor: bash
data: aws iam list-policy-versions --policy-arn $_POLICY_ARN
output: null
created_at: '2023-04-06T03:56:10.313396+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - iam
  - discovery
  - enumeration
verified: true
validated: true
---

# aws-iam-list-policy-versions

## Command

```bash
aws iam list-policy-versions --policy-arn $_POLICY_ARN
```

## Description

This command queries the AWS IAM service to list all versions of a specified managed policy, including version IDs, creation dates, and default status. Use it during cloud discovery to audit policy evolution and spot permission weaknesses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --policy-arn $_POLICY_ARN | The Amazon Resource Name (ARN) of the IAM policy (e.g., arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess) | Yes |

## Examples

### Basic Usage

```bash
aws iam list-policy-versions --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

### Advanced Usage

```bash
aws iam list-policy-versions --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess --output json --query 'Versions[*].[VersionId,CreateDate,IsDefaultVersion]'
```

This filters output to show only version ID, creation date, and default status in JSON format.

## Expected Output

Successful execution returns JSON like:

```json
{
    "Versions": [
        {
            "VersionId": "v1",
            "Document": null,
            "IsDefaultVersion": true,
            "CreateDate": "2023-01-01T12:00:00+00:00"
        },
        {
            "VersionId": "v2",
            "Document": null,
            "IsDefaultVersion": false,
            "CreateDate": "2023-02-01T12:00:00+00:00"
        }
    ]
}
```

Look for multiple versions indicating changes; the default version is active. Errors like "AccessDenied" indicate insufficient permissions.

## Related

- [[Related Procedure: Enumerate-AWS-IAM-Managed-Policy-Versions]]
- [[Related Command: aws-iam-list-policies]]
