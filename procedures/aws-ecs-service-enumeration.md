---
id: 29ef8da6-243d-4793-a178-b0430a719cda
name: aws-ecs-service-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.715435+00:00'
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
  - '[[tags/Listing information about a specific service]]'
commands:
  - '[[commands/list-ecs-clusters]]'
  - '[[commands/describe-ecs-service]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS ECS Service Enumeration

## Summary

This procedure enumerates AWS Elastic Container Service (ECS) services to gather detailed information about specific services within a cluster, including service names, ARNs, launch types, status, task definitions, and associated tasks. It is useful for discovering potential misconfigurations, identifying running workloads, and mapping the cloud environment during reconnaissance or auditing.

## Description

AWS ECS is a container orchestration service that manages Docker containers on EC2 instances or Fargate. Enumerating services reveals operational details like desired vs. running task counts, load balancers, and health checks, which can expose vulnerabilities such as over-privileged services or exposed ports. In offensive scenarios, this helps identify targets for lateral movement or exploitation. Defensively, it aids in verifying service configurations and detecting unauthorized changes. The procedure uses AWS CLI commands to query the ECS API, requiring appropriate IAM permissions like ecs:DescribeServices and ecs:ListClusters.

## Requirements

1. Valid AWS credentials with IAM permissions for ecs:ListClusters, ecs:DescribeServices, and ecs:DescribeClusters.
2. AWS CLI version 2 or later installed and configured with access keys or IAM role.
3. Network access to AWS endpoints (no VPC restrictions blocking API calls).
4. Optional: jq for parsing JSON output if scripting further analysis.

## Defense

- Implement least-privilege IAM policies to restrict ecs:Describe* actions to necessary roles only.
- Enable AWS CloudTrail logging for ECS API calls to monitor enumeration attempts.
- Use AWS Config rules to alert on unexpected service descriptions or changes.
- Rotate credentials regularly and monitor for anomalous API usage via GuardDuty.

## Objectives

1. Identify ECS services and their configurations for vulnerability assessment.
2. Map cluster dependencies and task details to understand the environment.
3. Verify service health and scaling to detect misconfigurations.

## Instructions

### Step 1: List ECS Clusters

**Context**: Before enumerating services, identify available ECS clusters to select the target cluster. This step ensures you have the correct cluster name for subsequent queries.

**Command** ([[commands/list-ecs-clusters]]):
```bash
aws ecs list-clusters --region $_AWS_REGION
```

> This command queries the ECS API for all clusters in the specified region. Review the output to note cluster ARNs or names. If no clusters are returned, confirm permissions or check if ECS is used in the environment.

### Step 2: Describe Specific ECS Service

**Context**: Use the cluster name from Step 1 to retrieve detailed information about a target service, including status, task definitions, and health metrics. This reveals potential attack surfaces like exposed container ports.

**Command** ([[commands/describe-ecs-service]]):
```bash
aws ecs describe-services --cluster $_CLUSTER_NAME --services $_SERVICE_NAME --region $_AWS_REGION
```

> The output is a JSON structure with service details. Parse it to extract ARN, launch type (EC2/Fargate), desired/running counts, and task ARNs. If the service doesn't exist, you'll get an empty services array—verify the name with list-services if needed.

### Step 3: Parse and Analyze Output

**Context**: Optionally, pipe the output to jq for filtered analysis, such as extracting task definitions or load balancer info, to focus on key intelligence.

**Command** ([[commands/describe-ecs-service]] with jq):
```bash
aws ecs describe-services --cluster $_CLUSTER_NAME --services $_SERVICE_NAME --region $_AWS_REGION | jq '.services[0]'
```

> This filters the JSON to the first service object. Look for fields like 'taskDefinition', 'loadBalancers', and 'healthCheckGracePeriodSeconds' to identify misconfigurations, such as public load balancers.
