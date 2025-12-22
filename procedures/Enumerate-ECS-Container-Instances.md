---
id: 9eef2f06-db48-4b56-aa42-579816eca49f
name: Enumerate-ECS-Container-Instances
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.812949+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/ECS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing all containers in specified cluster]]'
commands:
  - '[[commands/aws-ecs-list-container-instances]]'
platforms:
  - AWS
tools: []
validated: true
---

# Enumerate-ECS-Container-Instances

## Summary

This procedure uses the AWS CLI to list all container instances in a specified ECS cluster, providing visibility into the running containers and their ARNs for further discovery and potential targeting in a cloud environment.

## Description

In an AWS ECS (Elastic Container Service) environment, attackers with compromised credentials can enumerate container instances to map the infrastructure, identify running workloads, and spot opportunities for lateral movement or data exfiltration. This technique falls under system information discovery as it reveals details about container orchestration without direct host access. The procedure requires authenticated access to the ECS service via AWS CLI and assumes the attacker knows or has enumerated the target cluster name beforehand. Successful execution returns a list of container instance ARNs, which can be used in subsequent API calls for deeper inspection, such as describing tasks or services.

## Requirements

1. Valid AWS credentials with permissions to call `ecs:ListContainerInstances` (e.g., attached to an IAM role or user with ECS read access).
2. AWS CLI installed and configured with the target account's credentials (via `aws configure` or environment variables).
3. Knowledge of the target ECS cluster name.
4. Network access to AWS APIs (no direct VPC access needed if using public endpoints).

## Defense

- Implement least-privilege IAM policies to restrict `ecs:ListContainerInstances` to only necessary roles.
- Enable AWS CloudTrail logging for ECS API calls and monitor for unauthorized enumeration attempts.
- Use AWS Organizations SCPs to deny broad ECS access across accounts.
- Rotate credentials regularly and monitor for anomalous API activity via GuardDuty or CloudWatch.

## Objectives

1. Retrieve a list of all container instances in the target ECS cluster.
2. Identify ARNs for further enumeration of tasks, services, or container details.
3. Map the containerized workload environment for targeted exploitation.

## Instructions

### Step 1: List Container Instances

**Context**: This step queries the ECS service to retrieve ARNs of all container instances in the specified cluster, providing an overview of active infrastructure components.

**Command** ([[commands/aws-ecs-list-container-instances]]):
```bash
aws ecs list-container-instances --cluster $_CLUSTER_NAME
```

> This command sends a request to the ECS API and returns JSON output listing container instance ARNs. Replace `$_CLUSTER_NAME` with the actual cluster name (e.g., "my-cluster"). If the cluster has no instances, an empty array is returned. Verify success by checking for the `containerInstanceArns` field in the response. Use output formatting like `--output table` for readability if needed.
