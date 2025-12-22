---
type: command
executor: bash
data: aws cloudformation list-stack-sets
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - cloudformation
  - discovery
verified: true
validated: true
---

# aws-cloudformation-list-stack-sets

## Command

```bash
aws cloudformation list-stack-sets
```

## Description

Retrieves a list of CloudFormation stack sets in the account. Tests permissions for managing infrastructure-as-code deployments, indicating potential for template-based attacks if accessible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Uses default region; specify --region if needed | No |

## Examples

### Basic Usage

```bash
aws cloudformation list-stack-sets
```

### In Specific Region

```bash
aws cloudformation list-stack-sets --region us-east-1
```

## Expected Output

JSON {"Summaries": [{"StackSetId": "stackset-123", "Status": "ACTIVE"}]}. Access denied if insufficient perms.

## Related

- [[procedures/AWS-IAM-Permissions-Enumeration]]
