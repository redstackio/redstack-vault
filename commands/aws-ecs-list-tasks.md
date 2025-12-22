---
id: 6a5d1b6d-300d-452a-8a3a-2117108c6e44
type: command
executor: bash
data: aws ecs list-tasks --cluster $_CLUSTER_NAME
output: null
created_at: '2023-04-06T03:56:12.743446+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tags:
  - cloud-aws
  - ecs
  - enumeration
verified: true
validated: true
---

# AWS ECS List Tasks

## Command

```bash
aws ecs list-tasks --cluster $_CLUSTER_NAME
```

## Description

This command queries the AWS ECS API to list all task ARNs running in the specified cluster, aiding in discovery of active container workloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster $_CLUSTER_NAME | The name of the ECS cluster to query (e.g., "default" or "production-cluster") | Yes |

## Examples

### Basic Usage

```bash
aws ecs list-tasks --cluster default
```

### With Output Formatting

```bash
aws ecs list-tasks --cluster my-cluster --output table
```

## Expected Output

Successful execution returns JSON with task ARNs:

```json
{
    "taskArns": [
        "arn:aws:ecs:us-east-1:123456789012:task/my-cluster/abc123def456",
        "arn:aws:ecs:us-east-1:123456789012:task/my-cluster/ghi789jkl012"
    ],
    "failures": []
}
```

If no tasks are running:

```json
{
    "taskArns": [],
    "failures": []
}
```

## Related

- [[procedures/aws-ecs-task-enumeration]]
- [[tools/aws-cli]]
