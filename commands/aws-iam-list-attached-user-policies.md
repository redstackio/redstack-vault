---
id: 6fb649b9-2223-4724-ad0c-2026e5ca0070
name: aws-iam-list-attached-user-policies
type: command
executor: bash
data: aws iam list-attached-user-policies --user-name $_USERNAME
output: null
created_at: '2023-04-06T03:56:12.232556+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-list-attached-user-policies

## Command

```bash
aws iam list-attached-user-policies --user-name $_USERNAME
```

## Description

This command queries AWS IAM to list all managed policies attached to a specific user. It is used during cloud reconnaissance to map user permissions and identify over-privileged accounts. The output is JSON-formatted, detailing policy attachments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--user-name $_USERNAME` | The name of the IAM user (e.g., `john.doe`) whose attached policies to list | Yes |
| `--profile $_PROFILE` (optional) | AWS profile to use for authentication if not default | No |
| `--region $_REGION` (optional) | AWS region (default: us-east-1) | No |

## Examples

### Basic Usage

```bash
aws iam list-attached-user-policies --user-name john.doe
```

### With Output Parsing

```bash
aws iam list-attached-user-policies --user-name john.doe | jq '.AttachedPolicies[].PolicyName'
```

### Advanced Usage

```bash
aws iam list-attached-user-policies --user-name john.doe --profile my-aws-profile --region us-west-2
```

## Expected Output

Successful execution returns a JSON object like:

```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        },
        {
            "PolicyName": "CustomS3ReadOnly",
            "PolicyArn": "arn:aws:iam::123456789012:policy/CustomS3ReadOnly"
        }
    ],
    "IsTruncated": false
}
```

If no policies are attached:

```json
{
    "AttachedPolicies": []
}
```

Errors include `AccessDenied` if permissions are insufficient.

## Related

- [[procedures/Enumerate-IAM-User-Attached-Policies]]
- [[tools/AWS-CLI]]
