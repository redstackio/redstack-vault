---
id: 71235a34-1ef0-4f3c-9140-1d7a65719e08
name: describe-ecs-service
type: command
executor: bash
data: >-
  aws ecs describe-services --cluster $_CLUSTER_NAME --services $_SERVICE_NAME
  --region $_AWS_REGION
output: null
created_at: '2023-04-06T03:56:12.711424+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - enumeration
  - cloud
verified: true
validated: true
---

# Describe ECS Service

## Command

```bash
aws ecs describe-services --cluster $_CLUSTER_NAME --services $_SERVICE_NAME --region $_AWS_REGION
```

## Description

This command retrieves detailed information about one or more ECS services in a specified cluster, including configuration, status, and task details. Ideal for reconnaissance to uncover service vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cluster $_CLUSTER_NAME | Name or ARN of the ECS cluster | Yes |
| --services $_SERVICE_NAME | Name or list of service names/ARNs (comma-separated) | Yes |
| --region $_AWS_REGION | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws ecs describe-services --cluster my-cluster --services my-service --region us-east-1
```

### Advanced Usage

```bash
aws ecs describe-services --cluster my-cluster --services service1,service2 --region us-east-1 --output json
```

## Expected Output

```
{
    "services": [
        {
            "serviceArn": "arn:aws:ecs:us-east-1:123456789012:service/my-cluster/my-service",
            "serviceName": "my-service",
            "status": "ACTIVE",
            "desiredCount": 2,
            "runningCount": 2,
            "taskDefinition": "arn:aws:ecs:us-east-1:123456789012:task-definition/my-task:1",
            "launchType": "FARGATE"
        }
    ],
    "failures": []
}
```

Success shows a 'services' array with details; failures array indicates errors like invalid service names.

## Related

- [[procedures/aws-ecs-service-enumeration]]
- [[tools/aws-cli]]
