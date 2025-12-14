---
data: 'aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2'
tags:
  - aws
  - permission-test
type: command
output: '{"agentSummaries": []}'
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.775Z'
id: 5135c59d-8e5f-489d-9334-39da7cb399e6
verified: false
validated: true
submitted: true
---
# aws-bedrock-agent-list-agents-nonprod-admin

## Command

```bash
aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2
```

## Description

Tests successful permission access on non-production endpoint with admin profile.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region | Yes |
| `--endpoint-url` | Non-production URL | Yes |

## Examples

### With Admin Profile

```bash
AWS_PROFILE=admin aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2
```

## Expected Output

{"agentSummaries": []}; no CloudTrail log.

## Related

- [[commands/aws-bedrock-agent-list-agents-nonprod-noperm]]
- [[procedures/Enumerate-IAM-Permissions-via-Profile-Switching]]
