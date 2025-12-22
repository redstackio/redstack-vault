---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
type: command
executor: bash
data: aws iam list-users --output table
output: null
created_at: '2023-04-06T03:56:13.431244+00:00'
updated_at: '2024-10-01T00:00:00+00:00'
platforms:
  - AWS
tags:
  - iam
  - enumeration
  - discovery
verified: true
validated: true
---

# AWS-IAM-List-Users

## Command

```bash
aws iam list-users --output table
```

## Description

This command lists all IAM users in the current AWS account, displaying key details in a readable table format. Use it during reconnaissance to map user accounts after gaining initial API access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--output table` | Formats the response as a human-readable table | No |

## Examples

### Basic Usage

```bash
aws iam list-users --output table
```

### JSON Output (Default)

```bash
aws iam list-users
```

## Expected Output

```
-------------------
|    ListUsers    |
+-----------------+
|  Users          |
+-----------------+
|  Arn            |
|  CreateDate     |
|  Path           |
|  UserId         |
|  UserName       |
+-----------------+

```

A table listing users, or JSON array on error/denial.

## Related

- [[commands/aws-sts-get-caller-identity]]
- [[procedures/AWS-IAM-User-Enumeration-and-Credential-Checking]]
