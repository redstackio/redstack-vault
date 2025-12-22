---
id: 29b16867-e5b5-4e5a-b5cc-02fe36646523
type: command
executor: bash
data: aws iam list-group-policies --group-name $_GROUP_NAME
output: null
created_at: '2023-04-06T03:56:10.162594+00:00'
updated_at: '2023-04-10T20:20:11.157858+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - aws
  - iam
  - discovery
  - cloud
verified: true
validated: true
---

# aws-iam-list-group-policies

## Command

```bash
aws iam list-group-policies --group-name $_GROUP_NAME
```

## Description

This command lists the names of inline policies embedded in the specified IAM group. It helps discover permissions granted to the group without retrieving full policy details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --group-name $_GROUP_NAME | The name of the IAM group to query (e.g., "Admins") | Yes |

## Examples

### Basic Usage

```bash
aws iam list-group-policies --group-name Admins
```

### With Output Formatting

```bash
aws iam list-group-policies --group-name Developers --output table
```

## Expected Output

```
{
    "PolicyNames": [
        "InlineAdminPolicy",
        "ReadOnlyPolicy"
    ]
}
```

An empty "PolicyNames" array indicates no inline policies. Use jq for easier parsing: `| jq '.PolicyNames'`. Errors occur if the group doesn't exist or permissions are insufficient.

## Related

- [[procedures/AWS-IAM-Group-Inline-Policies-Enumeration]]
- [[tools/aws-cli]]
