---
data: >-
  aws bedrock-agent list-knowledge-bases --endpoint-url [redacted] --region
  us-west-2
tags:
  - aws
  - bedrock-agent
type: command
output: InternalServerErrorException
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.780Z'
id: 8b2e18a2-2e13-4fb7-8413-24c65f3d6a1f
verified: false
validated: true
submitted: true
---
# aws-bedrock-agent-list-knowledge-bases-nonprod

## Command

```bash
aws bedrock-agent list-knowledge-bases --endpoint-url [redacted] --region us-west-2
```

## Description

Lists knowledge bases on a non-production endpoint to verify functionality and lack of logging post-initial fixes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region | Yes |
| `--endpoint-url` | Non-production URL | Yes |

## Examples

### Basic Usage

```bash
aws bedrock-agent list-knowledge-bases --endpoint-url [redacted] --region us-west-2
```

## Expected Output

InternalServerErrorException due to max retries; no CloudTrail log.

## Related

- [[commands/aws-bedrock-agent-list-agents-nonprod]]
- [[procedures/Test-Non-Production-Endpoint-Silent-Calls]]
