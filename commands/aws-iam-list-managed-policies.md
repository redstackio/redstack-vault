---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: aws-iam-list-managed-policies
type: command
executor: bash
data: >-
  aws iam list-policies --scope AWS --query
  'Policies[].{PolicyName:PolicyName,Arn:Arn}' --output table
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - AWS
tags:
  - iam
  - discovery
verified: true
validated: true
---

# aws-iam-list-managed-policies

## Command

```bash
aws iam list-policies --scope AWS --query 'Policies[].{PolicyName:PolicyName,Arn:Arn}' --output table
```

## Description

This command lists all AWS-managed IAM policies, filtering to those created by AWS. It uses JMESPath querying to display only policy names and ARNs in a table format for quick review during discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --scope AWS | Limits results to AWS-managed policies (vs. Local for customer-managed) | Yes |
| --query 'Policies[].{PolicyName:PolicyName,Arn:Arn}' | JMESPath expression to select and format output fields | No (but recommended for clarity) |
| --output table | Formats output as a human-readable table | No (default is JSON) |

## Examples

### Basic Usage

```bash
aws iam list-policies --scope AWS
```

### Advanced Usage

```bash
aws iam list-policies --scope AWS --query 'Policies[?PolicyName==`AmazonS3ReadOnlyAccess`].Arn' --output text
```

## Expected Output

```
---------------------------------------
|             ListPolicies             |
+-------------------------------------+
| PolicyName      |      Arn           |
+-------------------------------------+
| AmazonEC2ReadOnlyAccess | arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess |
| AmazonS3ReadOnlyAccess  | arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess  |
+-------------------------------------+
```

## Related

- [[procedures/Enumerate-AWS-Managed-IAM-Policies]]
- [[tools/aws-cli]]
