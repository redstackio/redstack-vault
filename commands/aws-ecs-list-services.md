---
id: 59e7711e-0664-4d2c-9dcd-10a3d2053a86
name: aws-ecs-list-services
type: command
executor: bash
data: aws ecs list-services --cluster $_CLUSTER_NAME
output: null
created_at: '2023-04-06T03:56:12.685983+00:00'
updated_at: '2023-04-10T20:20:48.156668+00:00'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tags:
  - cloud
  - enumeration
  - ecs
verified: true
validated: true
---

# AWS ECS List Services

## Command

```bash
aws ecs list-services --cluster $_CLUSTER_NAME
```

## Description

This command queries the AWS ECS API to list all services in a specified cluster, returning their ARNs. Use it during cloud discovery to map container services for potential exploitation or auditing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster $_CLUSTER_NAME | The name of the ECS cluster to query (e.g., "default" or "prod-cluster") | Yes |
| --region | AWS region (defaults to configured region, e.g., us-east-1) | No |
| --output | Output format (json, table, text; defaults to json) | No |

## Examples

### Basic Usage

```bash
aws ecs list-services --cluster my-cluster
```

### With Region and JSON Output

```bash
aws ecs list-services --cluster my-cluster --region us-west-2 --output json
```

## Expected Output

Successful execution returns JSON like:

```json
{
    "services": [
        "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/web-service",
        "arn:aws:ecs:us-west-2:123456789012:service/my-cluster/db-service"
    ]
}
```

If the cluster has no services, "services" is an empty array. Errors include AccessDenied if permissions are insufficient.

## Related

- [[aws-ecs-describe-services]]
- [[procedures/aws-ecs-services-enumeration]]
