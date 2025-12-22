---
id: 7d297055-e60b-411c-834b-bf8b47f74fdd
name: aws-ecs-list-container-instances
type: command
executor: bash
data: aws ecs list-container-instances --cluster $_CLUSTER_NAME
output: null
created_at: '2023-04-06T03:56:12.808357+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - aws
  - ecs
verified: true
validated: true
---

# aws-ecs-list-container-instances

## Command

```bash
aws ecs list-container-instances --cluster $_CLUSTER_NAME
```

## Description

This command lists the Amazon Resource Names (ARNs) of all container instances in the specified ECS cluster, aiding in discovery of running container infrastructure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster $_CLUSTER_NAME | The short name or full ARN of the ECS cluster to query. Use the cluster name for simplicity. | Yes |

## Examples

### Basic Usage

```bash
aws ecs list-container-instances --cluster my-production-cluster
```

### Advanced Usage

```bash
aws ecs list-container-instances --cluster my-production-cluster --output table
```

## Expected Output

Successful execution returns JSON with a list of container instance ARNs:

```json
{
    "containerInstanceArns": [
        "arn:aws:ecs:us-east-1:123456789012:container-instance/abc123",
        "arn:aws:ecs:us-east-1:123456789012:container-instance/def456"
    ]
}
```

If no instances exist, the array is empty. Errors occur if credentials lack permissions or the cluster does not exist (e.g., "ClusterNotFoundException").

## Related

- [[procedures/Enumerate-ECS-Container-Instances]]
