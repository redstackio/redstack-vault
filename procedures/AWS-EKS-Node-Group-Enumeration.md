---
id: c7fe3bc4-5c6d-4128-ac01-9bf4e3113a3b
name: AWS-EKS-Node-Group-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.887349+00:00'
updated_at: '2023-04-10T20:20:06.996359+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - cloud-aws
  - eks
  - enumeration
  - list-nodegroups
commands:
  - '[[commands/aws-eks-list-nodegroups]]'
platforms:
  - AWS
  - Cloud
tools: []
validated: true
---

# AWS-EKS-Node-Group-Enumeration

## Summary

This procedure enumerates all node groups associated with a specified Amazon Elastic Kubernetes Service (EKS) cluster using the AWS CLI. It retrieves a list of node group names, providing visibility into the cluster's worker node infrastructure, which can help attackers map the environment for lateral movement or privilege escalation opportunities.

## Description

Amazon EKS is a managed Kubernetes service that simplifies running Kubernetes clusters on AWS. Node groups represent the underlying EC2 instances that serve as worker nodes for the cluster. Enumerating these node groups reveals the scale, configuration, and potential vulnerabilities in the cluster's compute resources. This technique is part of cloud service discovery, allowing attackers with compromised AWS credentials to gather intelligence on the infrastructure without direct access to the Kubernetes control plane. It is particularly useful in red team engagements to identify targets for further exploitation, such as targeting misconfigured node IAM roles, or for blue teams to audit cluster configurations.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least `eks:ListNodegroups` permission on the target cluster.
2. AWS CLI installed and configured with the appropriate profile (e.g., via `aws configure`).
3. Network access to AWS API endpoints (typically over HTTPS on port 443).
4. Knowledge of the target EKS cluster name.

## Defense

- Implement least privilege access for IAM roles and users, restricting `eks:ListNodegroups` to only necessary personnel.
- Enable AWS CloudTrail logging for EKS API calls to detect unauthorized enumeration attempts.
- Use AWS Organizations SCPs to limit discovery actions across accounts.
- Monitor for anomalous API calls from unexpected IP addresses or user agents.

## Objectives

1. Retrieve a complete list of node groups in the specified EKS cluster.
2. Identify node group names for potential follow-on targeting, such as instance metadata access or scaling attacks.
3. Verify cluster infrastructure details without alerting monitoring if credentials are low-privilege.

## Instructions

### Step 1: Configure AWS CLI Credentials

**Context**: Ensure the AWS CLI is set up with credentials that have the necessary permissions to query EKS resources. This step authenticates the session and sets the default region if not already configured.

Run `aws configure` to set your access key, secret key, default region (e.g., us-east-1), and output format (json).

> This prepares the environment for API calls. Expected output: No output if successful; credentials are stored in ~/.aws/credentials.

### Step 2: List Node Groups in the EKS Cluster

**Context**: Execute the AWS CLI command to query the EKS service for all node groups associated with the target cluster. This retrieves the names of managed or self-managed node groups.

**Command** ([[commands/aws-eks-list-nodegroups]]):

```bash
aws eks list-nodegroups --cluster-name $_CLUSTER_NAME
```

> Replace $_CLUSTER_NAME with the actual EKS cluster name (e.g., my-cluster). This sends a GET request to the EKS API and returns a JSON response with a 'nodegroups' array. If the cluster has no node groups, the array will be empty.

### Step 3: Parse and Verify Output

**Context**: Review the JSON output to confirm the list of node groups and check for any errors. Optionally, pipe the output to jq for formatted viewing or extraction.

**Command** ([[commands/aws-eks-list-nodegroups]]):

```bash
aws eks list-nodegroups --cluster-name $_CLUSTER_NAME | jq '.nodegroups[]'
```

> This step validates the discovery and extracts individual node group names. Expected output: A list of node group names or an empty list if none exist. Errors like 'AccessDenied' indicate insufficient permissions.
