---
data: 'aws bedrock-agent list-agents --region us-west-2 --endpoint-url [redacted]'
tags:
  - aws
  - non-production
type: command
output: JSON response or error; no CloudTrail log
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.782Z'
id: 89363180-448a-4782-9d63-7b15b013689d
verified: false
validated: true
submitted: true
---
# aws-bedrock-agent-list-agents-nonprod

## Command

```bash
aws bedrock-agent list-agents --region us-west-2 --endpoint-url [redacted]
```

## Description

Lists Bedrock agents using a non-production endpoint override, testing for silent execution without CloudTrail logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region | Yes |
| `--endpoint-url` | Custom non-production URL | Yes |

## Examples

### Basic Usage

```bash
aws bedrock-agent list-agents --region us-west-2 --endpoint-url [redacted]
```

### With Profile

```bash
AWS_PROFILE=admin aws bedrock-agent list-agents --region us-west-2 --endpoint-url [redacted]
```

## Expected Output

{"agentSummaries": []} or AccessDeniedException; no log in CloudTrail.

## Related

- [[commands/aws-bedrock-agent-list-agents-production]]
- [[procedures/Test-Non-Production-Endpoint-Silent-Calls]]
