---
id: ef3d936e-43cf-411b-8beb-bbcfead08791
name: aws-iam-list-all-policies
type: command
executor: bash
data: aws iam list-policies
output: null
created_at: '2023-04-06T03:56:10.262657+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - cloud-aws
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-list-all-policies

## Command

```bash
aws iam list-policies
```

## Description

This command retrieves a list of all IAM policies in the current AWS account, including both AWS-managed and customer-managed policies. It is used during cloud reconnaissance to map permissions and identify potential misconfigurations without any filtering applied.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Lists all policies by default; no positional arguments needed | No |
| --scope $_SCOPE | Filters by policy scope (Local for customer policies, AWS for managed); e.g., --scope Local | No |
| --path-prefix $_PATH_PREFIX | Filters policies by path prefix; e.g., --path-prefix /division/ | No |
| --query $_QUERY | JMESPath query to customize output; e.g., --query 'Policies[].PolicyName' | No |
| --output $_FORMAT | Output format (json, text, table); defaults to json | No |

## Examples

### Basic Usage

```bash
aws iam list-policies
```

### Filter to Local Policies Only

```bash
aws iam list-policies --scope Local --query 'Policies[].{Name:PolicyName, Arn:Arn}'
```

### Advanced Usage

```bash
aws iam list-policies --path-prefix /admin/ --output table
```

## Expected Output

Successful execution returns a JSON object with a Policies array containing policy details:

```json
{
    "Policies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyId": "ANPAZKIPA",
            "Arn": "arn:aws:iam::aws:policy/AdministratorAccess",
            "Path": "/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 5,
            "IsAttachable": true,
            "Description": "Provides full access to AWS services",
            "CreateDate": "2019-12-01T00:00:00+00:00",
            "UpdateDate": "2020-01-01T00:00:00+00:00"
        }
    ],
    "IsTruncated": false
}
```

If no policies exist or permissions are insufficient, it returns an empty Policies array or an AccessDenied error.

## Related

- [[procedures/AWS-IAM-Policy-Enumeration]]
- [[commands/aws-iam-list-attached-policies]]
