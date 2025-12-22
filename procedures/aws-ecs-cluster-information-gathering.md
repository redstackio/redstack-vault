---
id: dbc869b8-26b2-4e3d-9ca3-56887c6f3e7c
name: aws-ecs-cluster-information-gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.665879+00:00'
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
  - '[[tags/Listing information about a specific cluster]]'
commands:
  - '[[commands/aws-ecs-describe-clusters]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS ECS Cluster Information Gathering

## Summary

This procedure uses the AWS CLI to retrieve detailed information about a specific ECS (Elastic Container Service) cluster, including its ARN, status, registered container instances, and associated services. It enables attackers with compromised AWS credentials to map the cluster's structure, identify running instances, and assess resource utilization for potential lateral movement or privilege escalation in cloud environments.

## Description

In an AWS environment, ECS clusters manage containerized workloads. An attacker with read access to ECS can enumerate cluster details to understand the scale and configuration of the deployment, such as the number of container instances, their status (e.g., ACTIVE, DRAINING), CPU and memory reservations, and linked services or tasks. This discovery technique aligns with reconnaissance efforts to identify misconfigurations, like overly permissive IAM roles attached to tasks, or opportunities for container escape. The procedure relies on the `aws ecs describe-clusters` API call, which requires the `ecs:DescribeClusters` permission. It is typically used after initial credential compromise via methods like stolen access keys or assumed roles, and the output can inform subsequent actions like service enumeration or instance targeting.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least `ecs:DescribeClusters` permission on the target cluster.
2. Network access to AWS APIs (typically over HTTPS port 443) from the attacker's system.
3. AWS CLI version 2.x installed and configured with the target account's credentials via `aws configure`.

## Defense

- Implement least privilege access by restricting ECS permissions to only necessary roles and monitoring for anomalous API calls using AWS CloudTrail.
- Enable AWS Config rules to detect and alert on excessive ECS read permissions.
- Use IAM policies to deny `DescribeClusters` actions from untrusted IPs and integrate with SIEM for logging unusual ECS queries.

## Objectives

1. Retrieve comprehensive details on a specified ECS cluster's configuration and status.
2. Identify running container instances and resource allocations to spot potential vulnerabilities.
3. Gather intelligence for planning further cloud-based attacks, such as targeting specific services or tasks.

## Instructions

### Step 1: Configure AWS CLI and Verify Access

**Context**: Ensure the AWS CLI is set up with credentials that have ECS read permissions. This step verifies connectivity and permissions before querying the cluster.

Run the AWS CLI configure command if not already done, then test basic access with a simple ECS list-clusters call to confirm permissions without specifying a cluster.

**Command** ([[commands/aws-ecs-list-clusters]]):
```bash
aws ecs list-clusters
```

> This command lists all accessible ECS clusters in the current region. If it succeeds without errors, proceed; otherwise, check credentials and permissions. Expected output is a JSON array of cluster ARNs.

### Step 2: Describe the Target ECS Cluster

**Context**: Use the describe-clusters command to fetch detailed information about the specific cluster, including status, instances, and statistics. This reveals the cluster's operational state and scale.

Provide the cluster name (or ARN) as input. The command returns a JSON structure with cluster metadata, registered container instances (with their EC2 instance IDs if applicable), and capacity providers.

**Command** ([[commands/aws-ecs-describe-clusters]]):
```bash
aws ecs describe-clusters --cluster $_CLUSTER_NAME --region $_REGION
```

> Replace `$_CLUSTER_NAME` with the target cluster's name (e.g., 'my-production-cluster') and `$_REGION` with the AWS region (e.g., 'us-east-1'). If the cluster name is unknown, use Step 1 output to identify it. Expected output includes fields like `clusterArn`, `status`, `registeredContainerInstancesCount`, and `statistics` for CPU/memory usage.

### Step 3: Parse and Analyze Output

**Context**: Review the JSON response to extract key insights, such as instance counts or service ARNs, which can guide further enumeration (e.g., describing services via `aws ecs describe-services`).

Use `jq` or similar tools to filter the output for relevant fields. For example, extract the number of active instances.

**Command** (using jq for parsing):
```bash
aws ecs describe-clusters --cluster $_CLUSTER_NAME --region $_REGION | jq '.clusters[0].registeredContainerInstancesCount'
```

> This filters the response to show the instance count. Success is indicated by a numeric output greater than 0, confirming active resources in the cluster.
