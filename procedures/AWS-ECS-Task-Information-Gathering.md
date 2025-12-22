---
id: 33ec544c-b87c-48e2-b643-224f828687bf
name: AWS-ECS-Task-Information-Gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.785680+00:00'
updated_at: '2023-04-10T20:20:46.758288+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - aws
  - ecs
  - enumeration
  - cloud
  - discovery
commands:
  - '[[commands/aws-ecs-describe-tasks]]'
platforms:
  - AWS
tools: []
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# AWS-ECS-Task-Information-Gathering

## Summary

The AWS ECS Task Information Gathering procedure allows an attacker with valid AWS credentials to retrieve detailed metadata about specific tasks running in an Amazon ECS cluster. This includes task ARNs, status, CPU and memory usage, container definitions, and network configurations, which can reveal potential vulnerabilities such as exposed services or misconfigurations for further exploitation in cloud environments.

## Description

In an AWS environment, ECS (Elastic Container Service) manages containerized applications across clusters. Attackers who have compromised IAM credentials can use the AWS CLI to query ECS tasks, performing discovery to map the infrastructure. This procedure focuses on the 'describe-tasks' API call, which requires the ecs:DescribeTasks permission. It is typically used after initial access to AWS (e.g., via stolen keys) to understand running workloads without alerting defenders immediately. The output is JSON-formatted, allowing parsing for key details like container images (potential for image vulnerability scanning) or health checks. This technique aligns with system information discovery in cloud contexts, helping attackers identify high-value targets like production databases or web apps.

## Requirements

1. AWS CLI installed and configured with access keys or role assuming ECS permissions (at minimum, ecs:DescribeTasks).
2. Knowledge of the target ECS cluster name and at least one task ARN (obtainable via prior enumeration like listing tasks).
3. Network access to AWS APIs (no direct VPC access needed, but internet or VPC endpoint required).

## Defense

- Enforce least privilege IAM policies to restrict ecs:DescribeTasks to necessary roles only.
- Enable AWS CloudTrail logging for ECS API calls and monitor for anomalous queries (e.g., from unusual IPs or excessive calls).
- Use AWS GuardDuty or Config rules to detect unauthorized ECS metadata access and rotate credentials regularly.

## Objectives

1. Retrieve metadata on ECS tasks to map containerized workloads and identify misconfigurations.
2. Extract details like container images, ports, and volumes for targeted follow-on attacks.
3. Validate task status and resource usage to prioritize live, high-impact targets.

## Instructions

### Step 1: Verify AWS Configuration and Permissions

**Context**: Before querying tasks, ensure the AWS CLI is set up with credentials that have the required permissions. This step prevents errors from misconfiguration and confirms access to the ECS service.

Run `aws sts get-caller-identity` to verify your identity and then test ECS access with a lightweight call.

**Command** (not linked as it's prerequisite; use standard AWS CLI):
```bash
aws ecs list-clusters
```

> This lists available clusters without targeting specific tasks. If it succeeds, permissions are likely sufficient. Expected output: JSON array of cluster ARNs. If denied, adjust IAM policy.

### Step 2: Execute Task Description Query

**Context**: Use the describe-tasks command to fetch details on one or more specified tasks. This is the core action, providing actionable intelligence on task state and components. Provide the cluster name and task ARN(s); multiple ARNs can be queried in one call for efficiency.

**Command** ([[commands/aws-ecs-describe-tasks]]):
```bash
aws ecs describe-tasks --cluster $_CLUSTER_NAME --tasks $_TASK_ARN
```

> Replace $_CLUSTER_NAME with the target cluster (e.g., "default") and $_TASK_ARN with the task identifier (e.g., "arn:aws:ecs:us-east-1:123456789012:task/default/abc123def456"). The command returns a JSON structure with task details. If the task is stopped or invalid, check 'failures' array for errors.

### Step 3: Review and Parse Output for Insights

**Context**: Analyze the JSON response to extract key information like container logs, network bindings, or volumes. This step involves manual review or piping to tools like jq for filtering, enabling identification of attack vectors such as outdated images or open ports.

Use jq to filter specific fields (assuming jq is installed; this is a common post-processing step).

**Command** (standard jq; not a custom command):
```bash
aws ecs describe-tasks --cluster $_CLUSTER_NAME --tasks $_TASK_ARN | jq '.tasks[0].containers[0].image'
```

> Expected: The container image URI (e.g., "nginx:1.14"). Look for sensitive data in 'overrides', 'healthStatus', or 'networkBindings'. Success: No permission errors and relevant fields populated. If output is empty, verify task ARN.
