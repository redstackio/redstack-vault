---
data: aws bedrock-agent list-agents --region us-west-2
tags:
  - aws
  - bedrock-agent
type: command
output: JSON response with agent summaries; generates CloudTrail log
executor: bash
platforms:
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.786Z'
id: be11f4ca-f6fe-4602-9464-fe2b894dc53d
verified: false
validated: true
submitted: true
---
# aws-bedrock-agent-list-agents-production

## Command

```bash
aws bedrock-agent list-agents --region us-west-2
```

## Description

Lists Bedrock agents in the specified AWS region using the production endpoint, demonstrating standard logging to CloudTrail.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | Specifies the AWS region (e.g., us-west-2) | Yes |

## Examples

### Basic Usage

```bash
aws bedrock-agent list-agents --region us-west-2
```

### Advanced Usage

```bash
aws bedrock-agent list-agents --region us-west-2 --output table
```

## Expected Output

JSON array of agent summaries, e.g., {"agentSummaries": [...]}. CloudTrail log generated within 5-10 minutes.

## Related

- [[commands/aws-bedrock-agent-list-agents-nonprod]]
- [[procedures/Verify-Production-Endpoint-Logging]]
