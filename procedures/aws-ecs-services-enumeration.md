---
id: 558befc5-1f78-479a-a4c2-fd8655b6e5ee
name: aws-ecs-services-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.689812+00:00'
updated_at: '2023-04-10T20:20:48.132689+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/ECS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing all services in specified cluster]]'
commands:
  - '[[commands/aws-ecs-list-services]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS ECS Services Enumeration

## Summary

This procedure enumerates all services within a specified AWS Elastic Container Service (ECS) cluster using the AWS CLI. It retrieves a list of service ARNs, enabling attackers to map the container orchestration environment for identifying potential targets for exploitation, such as misconfigured services or entry points for lateral movement. Defenders can use this to audit cluster activity and detect unauthorized enumeration attempts.

## Description

AWS ECS is a scalable container orchestration service that manages Docker containers across EC2 instances or Fargate. Enumerating services in a cluster reveals the active workloads, their configurations, and potential vulnerabilities. This technique leverages the ECS ListServices API, which requires appropriate IAM permissions (e.g., ecs:ListServices). In an attack scenario, compromised credentials with read access to ECS allow discovery of running services, which could lead to further actions like inspecting task definitions or injecting malicious containers. From a defensive standpoint, logging API calls via CloudTrail can help identify anomalous enumeration. The procedure assumes AWS CLI v2 is installed and configured with valid credentials.

## Requirements

1. AWS CLI (version 2 or later) installed and configured with access keys or IAM role.
2. IAM permissions for ecs:ListServices action on the target cluster.
3. Network access to AWS endpoints (no VPC endpoints required for basic listing).
4. Knowledge of the target ECS cluster name.

## Defense

- Implement least-privilege IAM policies to restrict ecs:ListServices access to authorized roles only.
- Enable AWS CloudTrail logging for ECS API calls and monitor for unusual ListServices invocations from unexpected IPs or users.
- Use AWS Config rules to alert on over-permissive ECS policies and integrate with SIEM for anomaly detection.
- Segment ECS clusters with VPCs and security groups to limit lateral discovery.

## Objectives

1. Retrieve a complete list of service ARNs in the specified ECS cluster.
2. Identify running services for potential targeting or auditing.
3. Validate successful enumeration without triggering alerts.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials that have the necessary permissions to query ECS. This step confirms access before attempting enumeration.

Run the AWS configure list command to check current settings, then test basic ECS access with a describe-clusters command if needed.

**Command** ([[commands/aws-configure-list]]):
```bash
aws configure list
```

> This displays profile, region, and output format. Expected output includes current credential source (e.g., shared-credentials-file) and default region. If credentials are invalid, reconfigure using `aws configure`.

### Step 2: Enumerate ECS Services

**Context**: Use the AWS CLI to call the ListServices API, specifying the target cluster. This retrieves ARNs of all services, which can be used for deeper inspection.

**Command** ([[commands/aws-ecs-list-services]]):
```bash
aws ecs list-services --cluster $_CLUSTER_NAME
```

> Replace $_CLUSTER_NAME with the actual cluster name (e.g., "my-ecs-cluster"). The command outputs JSON with a "services" array containing ARNs. If no services exist, the array is empty. Verify by checking for HTTP 200 response and non-empty ARNs.

### Step 3: Parse and Review Output

**Context**: Process the JSON output to extract service details for analysis. This helps in identifying high-value services without additional API calls.

Use jq to filter the services array if available, or pipe to a file for manual review.

**Command** ([[commands/aws-ecs-list-services-with-jq]]):
```bash
aws ecs list-services --cluster $_CLUSTER_NAME | jq '.services[]'
```

> Assumes jq is installed. Expected output: Individual service ARNs printed line-by-line. Success if ARNs match known services or reveal unexpected ones.
