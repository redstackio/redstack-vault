---
id: 4072f3f4-b127-473c-9159-0c93518a3f27
name: aws-ecs-describe-tasks
type: command
executor: bash
data: aws ecs describe-tasks --cluster $_CLUSTER_NAME --tasks $_TASK_ARN
output: null
created_at: '2023-04-06T03:56:12.780944+00:00'
updated_at: '2023-04-10T20:20:46.786232+00:00'
platforms:
  - AWS
tags:
  - aws
  - ecs
  - discovery
verified: true
validated: true
---

# aws-ecs-describe-tasks

## Command

```bash
aws ecs describe-tasks --cluster $_CLUSTER_NAME --tasks $_TASK_ARN
```

## Description

This command queries the AWS ECS service to retrieve detailed information about one or more specified tasks in a given cluster. It is used for discovery in compromised AWS environments to understand running container workloads, including status, resources, and configurations. Requires AWS CLI v2 and appropriate IAM permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CLUSTER_NAME | The short name or full ARN of the ECS cluster containing the tasks | Yes |
| $_TASK_ARN | One or more ARNs of the tasks to describe (comma-separated or multiple flags; up to 100) | Yes |
| --cluster | Flag to specify the target cluster | Built-in |
| --tasks | Flag to specify the task ARNs | Built-in |

## Examples

### Basic Usage

Describe a single task:
```bash
aws ecs describe-tasks --cluster my-cluster --tasks arn:aws:ecs:us-east-1:123456789012:task/my-cluster/abc123
```

### Advanced Usage

Describe multiple tasks:
```bash
aws ecs describe-tasks --cluster my-cluster --tasks arn1 arn2 arn3
```

## Expected Output

The command outputs JSON describing the tasks. Successful response includes task details; failures are listed separately.

```
{
  "tasks": [
    {
      "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/my-cluster/abc123",
      "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
      "lastStatus": "RUNNING",
      "desiredStatus": "RUNNING",
      "cpu": "256",
      "memory": "512",
      "containers": [
        {
          "containerArn": "arn:...",
          "name": "my-container",
          "image": "nginx:1.21",
          "healthStatus": {
            "numTasksHealthy": 1
          },
          "networkBindings": [
            {
              "bindIP": "0.0.0.0",
              "containerPort": 80,
              "hostPort": 32768
            }
          ]
        }
      ]
    }
  ],
  "failures": []
}
```

Look for 'lastStatus' as RUNNING or STOPPED, and inspect 'containers' for exploitable images or ports.

## Related

- [[procedures/AWS-ECS-Task-Information-Gathering]]
