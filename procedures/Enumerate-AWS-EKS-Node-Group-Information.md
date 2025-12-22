---
id: e234dccc-617e-4a4a-be54-2cf1916c55bc
name: Enumerate-AWS-EKS-Node-Group-Information
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.911082+00:00'
updated_at: '2023-04-10T20:19:59.942257+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/EKS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing specific information about a node group in a cluster]]'
commands:
  - '[[commands/describe-eks-nodegroup]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
  - Kubernetes
skill_level: intermediate
impact_level: low
detection_risk: medium
validated: true
---

# Enumerate-AWS-EKS-Node-Group-Information

## Summary

This procedure uses the AWS CLI to enumerate detailed information about a specific node group in an Amazon EKS cluster, including node group name, instance types, scaling configuration, and status. It aids attackers in understanding the target's Kubernetes infrastructure for further discovery or targeting potential weaknesses in scaling and resource management.

## Description

Amazon Elastic Kubernetes Service (EKS) allows deployment and management of containerized applications on AWS using Kubernetes. During reconnaissance, an attacker with compromised AWS credentials can query node group details to map the cluster's compute resources. This reveals instance types (e.g., m5.large), auto-scaling settings (min/max/desired capacity), and health status, which can inform attacks like resource exhaustion or lateral movement within the cluster. The procedure requires permissions like eks:DescribeNodegroup and assumes the attacker has initial access to AWS via stolen keys or IAM roles. Success provides a JSON output that can be parsed for actionable intelligence on the environment.

## Requirements

1. Valid AWS credentials with at least eks:DescribeNodegroup permission on the target cluster.
2. AWS CLI installed and configured with the target's AWS profile (e.g., via `aws configure`).
3. Knowledge of the EKS cluster name and node group name, potentially obtained from prior enumeration like listing clusters.

## Defense

- Secure AWS credentials using IAM least privilege policies, avoiding broad EKS access.
- Enable AWS CloudTrail logging for EKS API calls and monitor for anomalous describe-nodegroup queries.
- Implement AWS Organizations SCPs to restrict EKS actions in sensitive environments.
- Use tools like AWS GuardDuty to detect unusual API activity from compromised credentials.

## Objectives

1. Retrieve specific details about an EKS node group, such as configuration and scaling parameters.
2. Identify potential targets within the cluster for further attacks, like exploiting misconfigured scaling.
3. Build a comprehensive map of the target's EKS infrastructure to support advanced persistence or disruption.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is set up with credentials that have access to the target EKS cluster. This step confirms authentication before querying sensitive resources.

Run `aws sts get-caller-identity` to verify your identity and permissions.

> If the output shows the expected account and role, proceed. Otherwise, update credentials.

### Step 2: Describe the EKS Node Group

**Context**: Execute the AWS CLI command to fetch detailed information about the specified node group. This reveals operational details useful for assessing the cluster's resilience and resource allocation.

**Command** ([[commands/describe-eks-nodegroup]]):
```bash
aws eks describe-nodegroup --cluster-name $_CLUSTER_NAME --nodegroup-name $_NODEGROUP_NAME
```

> Replace $_CLUSTER_NAME with the target EKS cluster name (e.g., my-cluster) and $_NODEGROUP_NAME with the node group name (e.g., my-nodegroup). The command returns a JSON structure containing node group metadata. Parse the output using jq for specific fields like instanceTypes or scalingConfig if needed.
