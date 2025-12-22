---
id: 99e15c01-38a4-45d9-a3c0-38c99259b6dc
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.749182+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/ECS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/AWS-CLI]]'
commands:
  - '[[commands/aws-ecs-list-tasks]]'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS ECS Task Enumeration

## Summary

This procedure enumerates running tasks within a specific Amazon ECS cluster using the AWS CLI, allowing attackers with valid credentials to identify active services, container configurations, and potential vulnerabilities for further exploitation in a cloud environment.

## Description

In an AWS environment, ECS (Elastic Container Service) manages containerized applications across clusters. Enumerating tasks reveals details about running workloads, such as task ARNs, which can be used to inspect container images, network settings, or even pivot to other resources. This technique requires authenticated access via AWS CLI and is commonly used during discovery phases to map the attack surface. It assumes the attacker has obtained credentials through prior compromise (e.g., via IAM role assumption or stolen keys). Success provides a list of task identifiers, enabling follow-on actions like describing tasks for deeper reconnaissance without alerting via excessive API calls.

## Requirements

1. Valid AWS credentials with at least read access to ECS (e.g., ecs:ListTasks permission)
2. AWS CLI installed and configured with the target account's credentials (via aws configure or environment variables)
3. Network access to AWS APIs (no direct VPC restrictions on CLI calls)
4. Knowledge of the target ECS cluster name

## Defense

- Implement least-privilege IAM policies to restrict ecs:ListTasks to necessary roles only
- Enable AWS CloudTrail logging for ECS API calls and monitor for unusual enumeration patterns from unexpected IPs or users
- Use AWS Organizations SCPs to limit cross-account access and rotate credentials regularly
- Integrate with SIEM tools to alert on high-volume ECS API queries

## Objectives

1. List all running tasks in a specified ECS cluster to identify active services
2. Gather task ARNs for potential follow-on enumeration (e.g., describe-tasks)
3. Map the cloud infrastructure for targeted exploitation of vulnerable containers

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials for the target account to avoid authentication errors during enumeration.

Run the following to check configuration:

```bash
aws sts get-caller-identity
```

> This command verifies your identity and account without performing the actual enumeration. If successful, it returns your user/role ARN and account ID.

### Step 2: List Tasks in the ECS Cluster

**Context**: Use the AWS CLI to query the ECS service for all tasks in the specified cluster, retrieving their ARNs for identification.

**Command** ([[commands/aws-ecs-list-tasks]]):

```bash
aws ecs list-tasks --cluster $_CLUSTER_NAME
```

> Replace $_CLUSTER_NAME with the actual cluster name (e.g., "my-production-cluster"). This returns a JSON response with a "taskArns" array listing unique identifiers for running tasks. If no tasks are running, the array will be empty.

### Step 3: Validate and Parse Output

**Context**: Review the output to confirm successful enumeration and prepare ARNs for further actions, such as describing individual tasks.

Use jq (if available) to parse the JSON:

```bash
aws ecs list-tasks --cluster $_CLUSTER_NAME | jq '.taskArns[]'
```

> This extracts just the task ARNs. Success is indicated by a non-empty list of ARNs, confirming active tasks in the cluster.
