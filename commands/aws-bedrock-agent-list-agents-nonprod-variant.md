---
data: 'aws bedrock-agent list-agents --endpoint-url [redacted]-2 --region us-west-2'
tags:
  - aws
  - variant-endpoint
type: command
output: '{"agentSummaries": []} or AccessDeniedException'
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.946Z'
id: 45c554fa-8722-43ed-bdc6-aeedbc6c913a
verified: false
validated: true
submitted: true
---
# aws-bedrock-agent-list-agents-nonprod-variant

## Command

```bash
aws bedrock-agent list-agents --endpoint-url [redacted]-2 --region us-west-2
```

## Description

Tests another non-production endpoint variant for permission enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region (implied us-west-2) | Yes |
| `--endpoint-url` | Variant non-production URL | Yes |

## Examples

### Basic Usage

```bash
aws bedrock-agent list-agents --endpoint-url [redacted]-2 --region us-west-2
```

## Expected Output

Success or denial based on profile; no CloudTrail log.

## Related

- [[commands/aws-bedrock-agent-list-agents-nonprod]]
- [[procedures/Enumerate-IAM-Permissions-via-Profile-Switching]]
