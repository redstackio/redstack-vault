---
id: cade7d49-c598-4429-a319-212b0cc9dc5a
name: aws-ecs-list-clusters
type: command
executor: bash
data: aws ecs list-clusters
output: null
created_at: '2023-04-06T03:56:12.636773+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - ecs
  - discovery
verified: true
validated: true
---

# aws-ecs-list-clusters

## Command

```bash
aws ecs list-clusters
```

## Description

This command queries the AWS ECS API to list all clusters in the current account and region. It returns ARNs of ECS clusters, useful for discovering container orchestration resources during reconnaissance. No specific cluster parameters are required, but global AWS options like region apply.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | AWS region to query (e.g., us-east-1) | No (uses default) |
| `--output` | Output format (json, table, text) | No (defaults to json) |
| `--profile` | AWS profile name for credentials | No (uses default) |
| `--no-paginate` | Disable automatic pagination for large results | No |

## Examples

### Basic Usage

```bash
aws ecs list-clusters
```

Returns JSON with cluster ARNs.

### Advanced Usage

```bash
aws ecs list-clusters --region us-west-2 --output table
```

Lists clusters in a specific region in table format for readability.

## Expected Output

```
{
    "clusterArns": [
        "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
        "arn:aws:ecs:us-east-1:123456789012:cluster/default"
    ]
}
```

If no clusters: {"clusterArns": []}. Errors occur if credentials lack ecs:ListClusters permission.

## Related

- [[procedures/Enumerate-AWS-ECS-Clusters]] (procedure that uses this command)
- [[tools/aws-cli]] (tool)
