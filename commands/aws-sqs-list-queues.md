---
type: command
executor: bash
data: aws sqs list-queues
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - sqs
  - discovery
verified: true
validated: true
---

# aws-sqs-list-queues

## Command

```bash
aws sqs list-queues
```

## Description

Lists all SQS queues in the account and region. This tests permissions for message queue discovery, potentially revealing sensitive data flows if accessible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Queues across all regions if multi-region setup | No |

## Examples

### Basic Usage

```bash
aws sqs list-queues
```

### With Max Results

```bash
aws sqs list-queues --max-results 10
```

## Expected Output

JSON {"QueueUrls": ["https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue"]} or empty. Denied if no perms.

## Related

- [[procedures/AWS-IAM-Permissions-Enumeration]]
