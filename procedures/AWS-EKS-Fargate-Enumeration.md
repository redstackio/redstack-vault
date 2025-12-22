---
id: 054791c3-e96b-43b0-8741-dce63f2bd765
name: AWS-EKS-Fargate-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.934109+00:00'
updated_at: '2023-04-10T20:20:42.392187+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud-AWS]]'
  - '[[tags/EKS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Fargate-Enumeration]]'
commands:
  - '[[commands/aws-eks-list-fargate-profiles]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-EKS-Fargate-Enumeration

## Summary

This procedure enables the enumeration of all Fargate profiles within a specified Amazon Elastic Kubernetes Service (EKS) cluster using the AWS CLI. Fargate profiles define how pods are deployed to Fargate, and enumerating them allows identification of container workloads, namespaces, and potential misconfigurations that could be exploited for further discovery or lateral movement in a cloud environment.

## Description

Amazon EKS Fargate provides a serverless compute engine for running Kubernetes pods without managing underlying infrastructure. In an attack scenario, an attacker with compromised AWS credentials may enumerate Fargate profiles to map the cluster's structure, discover running workloads, and pinpoint vulnerabilities such as overly permissive IAM roles attached to profiles or exposed container images. This technique falls under cloud service discovery, helping attackers understand the scope of accessible resources. The procedure relies on the AWS CLI's `eks` command group and requires appropriate permissions like `eks:ListFargateProfiles`. It is typically used after initial access to AWS via stolen credentials or misconfigured roles.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., access key ID and secret access key) that have `eks:ListFargateProfiles` permission on the target EKS cluster.
2. Network access to AWS APIs (typically over HTTPS on port 443).
3. Knowledge of the target EKS cluster name, which can be obtained via prior enumeration (e.g., listing EKS clusters with `aws eks list-clusters`).

## Defense

- Implement least privilege access by restricting IAM roles and users to only necessary EKS actions, using policies that deny `eks:ListFargateProfiles` for non-administrators.
- Enable AWS CloudTrail logging for EKS API calls and monitor for anomalous `ListFargateProfiles` requests, integrating with SIEM tools for alerts on unusual IP addresses or credential usage.
- Use network segmentation, such as VPC endpoints for EKS, to limit API access and prevent lateral movement from compromised instances.

## Objectives

1. Retrieve a complete list of Fargate profiles in the specified EKS cluster to map container deployment configurations.
2. Identify profile details like associated namespaces and IAM roles for potential exploitation vectors.
3. Validate successful enumeration to confirm access levels and inform subsequent attack steps, such as targeting specific pods.

## Instructions

### Step 1: Enumerate Fargate Profiles

**Context**: This step uses the AWS CLI to query the EKS service for all Fargate profiles in the target cluster. It provides visibility into serverless workloads without requiring direct cluster access, helping attackers assess the environment's scale and configurations. Ensure AWS credentials are active and the cluster name is known; if not, enumerate clusters first.

**Command** ([[commands/aws-eks-list-fargate-profiles]]):
```bash
aws eks list-fargate-profiles --cluster-name $_CLUSTER_NAME
```

> This command sends a request to the AWS EKS API and returns a JSON response listing Fargate profiles. The `--cluster-name` parameter specifies the target EKS cluster. If successful, it outputs profile names and ARNs; empty results indicate no profiles or insufficient permissions. Review the output for details like `fargateProfileName` and `podExecutionRoleArn` to identify exploitable elements. If the command fails with an access denied error, escalate privileges or pivot to another account.
