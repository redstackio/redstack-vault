---
id: a9b1fe79-fdff-430e-875f-8f133e5633c1
name: aws-iam-wildcard-policy-snippet
type: command
executor: bash
data: |-
  "Action": "*"
  "Resource": "*"
output: null
created_at: '2023-04-06T03:56:09.317572+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - policy
  - json
verified: true
validated: true
---

# aws-iam-wildcard-policy-snippet

## Command

```json
{
  "Action": "*",
  "Resource": "*"
}
```

## Description

JSON snippet for a wildcard statement in IAM policies granting full access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Action | Permissions ( * for all ) | Yes |
| Resource | Targets ( * for all ) | Yes |

## Examples

### Basic Usage

Embed in policy document.

## Expected Output

N/A - snippet for policy files.

## Related

- [[procedures/AWS-Shadow-Admin-Access]]
