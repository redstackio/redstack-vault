---
id: new-uuid-for-list-clusters
name: list-ecs-clusters
type: command
executor: bash
data: aws ecs list-clusters --region $_AWS_REGION
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - cloud
verified: true
validated: true
---

# List ECS Clusters

## Command

```bash
aws ecs list-clusters --region $_AWS_REGION
```

## Description

This command lists all ECS clusters in the specified AWS region, returning their ARNs. Use it as a starting point for ECS enumeration to identify clusters before describing services or tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_AWS_REGION | AWS region to query (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws ecs list-clusters --region us-east-1
```

### Advanced Usage

```bash
aws ecs list-clusters --region us-east-1 --output table
```

## Expected Output

```
{
    "clusterArns": [
        "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
        "arn:aws:ecs:us-east-1:123456789012:cluster/another-cluster"
    ]
}
```

A successful run returns a JSON array of cluster ARNs. Empty array indicates no clusters or insufficient permissions.

## Related

- [[procedures/aws-ecs-service-enumeration]]
- [[tools/aws-cli]]
