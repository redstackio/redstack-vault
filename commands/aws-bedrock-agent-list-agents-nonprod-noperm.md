---
data: 'aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2'
tags:
  - aws
  - denial-test
type: command
output: AccessDeniedException
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.948Z'
id: 70f08e9d-6bbc-4b19-9efb-953b420e4bf0
verified: false
validated: true
submitted: true
---
# aws-bedrock-agent-list-agents-nonprod-noperm

## Command

```bash
aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2
```

## Description

Tests failed permission on non-production endpoint with non-privileged profile.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region | Yes |
| `--endpoint-url` | Non-production URL | Yes |

## Examples

### With Noperm Profile

```bash
AWS_PROFILE=noperm aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2
```

## Expected Output

AccessDeniedException: User is not authorized to perform bedrock:ListAgents; no log.

## Related

- [[commands/aws-bedrock-agent-list-agents-nonprod-admin]]
- [[procedures/Enumerate-IAM-Permissions-via-Profile-Switching]]
