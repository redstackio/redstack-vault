---
id: aaf266b1-dca2-4370-af54-0f56e5757cd1
name: Enumerate-AWS-ECS-Clusters
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.640775+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526]]'
sub_techniques: []
tags:
  - aws
  - ecs
  - enumeration
  - cloud-discovery
commands:
  - '[[commands/aws-ecs-list-clusters]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate-AWS-ECS-Clusters

## Summary

This procedure enumerates all Amazon Elastic Container Service (ECS) clusters in a target AWS account using the AWS CLI. It provides attackers or security testers with visibility into container orchestration resources, enabling identification of running services, task definitions, and potential pivot points for further discovery or exploitation in cloud environments.

## Description

In AWS environments, ECS clusters manage containerized workloads using Docker or other runtimes. Enumerating these clusters reveals the structure of deployed applications, scales, and configurations without requiring elevated privileges beyond basic ECS read access. This technique aligns with cloud service discovery, allowing reconnaissance of infrastructure that could host sensitive data or services. The procedure leverages the AWS ECS API via the CLI to query cluster ARNs, which can then inform subsequent actions like inspecting tasks or services. It assumes configured AWS credentials with permissions like ecs:ListClusters and is most effective in accounts with active container deployments.

## Requirements

1. Valid AWS credentials with read access to ECS (e.g., IAM policy allowing ecs:ListClusters).
2. AWS CLI installed and configured with the target account's access key, secret key, and default region.
3. Network access to AWS endpoints (no VPC restrictions blocking CLI API calls).
4. Optional: jq installed for parsing JSON output.

## Defense

- Implement least privilege IAM policies to restrict ecs:ListClusters to necessary roles only.
- Enable AWS CloudTrail logging for ECS API calls and monitor for anomalous enumeration patterns from unexpected IPs or users.
- Use AWS Organizations SCPs to deny broad ECS discovery actions across accounts.
- Integrate with SIEM tools to alert on repeated ECS API queries indicating reconnaissance.

## Objectives

1. List all ECS cluster ARNs in the target AWS account.
2. Identify active container orchestration resources for further targeting.
3. Map the overall cloud infrastructure layout to support lateral movement or data collection.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials for the target account to avoid authentication errors during enumeration.

Run the AWS CLI configure list command to check current settings, then use aws configure if adjustments are needed (e.g., set default region to us-east-1).

**Command** ([[commands/aws-configure-list]]):
```bash
aws configure list
```

> This displays profile, access key status, and region. If credentials are invalid, reconfigure using aws configure with the target's access key ID, secret access key, and region. Expected output includes 'profile: default' and 'access_key: ******partial******' without errors.

### Step 2: Enumerate ECS Clusters

**Context**: Query the ECS service to retrieve a list of all clusters, providing ARNs that uniquely identify each cluster for follow-on operations like describing services or tasks.

Execute the list-clusters command to fetch the cluster inventory.

**Command** ([[commands/aws-ecs-list-clusters]]):
```bash
aws ecs list-clusters
```

> This API call returns a JSON array of cluster ARNs. If no clusters exist, it returns an empty array. Use --output table for human-readable format or pipe to jq for filtering (e.g., aws ecs list-clusters | jq '.clusterArns[]').

### Step 3: Parse and Validate Output

**Context**: Process the results to confirm successful enumeration and extract usable cluster names or ARNs for documentation or next steps.

Review the output for cluster ARNs, then optionally describe a specific cluster using its ARN to verify details.

**Command** ([[commands/aws-ecs-describe-clusters]]):
```bash
aws ecs describe-clusters --cluster CLUSTER_ARN
```

> Replace CLUSTER_ARN with a value from Step 2. Expected output is JSON with cluster details like status (ACTIVE), registered container instances, and settings. Success is indicated by non-empty clusterArns in Step 2 and ACTIVE status in descriptions.
