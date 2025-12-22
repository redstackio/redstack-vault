---
id: b26cb3ba-db40-40e7-98a8-46338e179cfa
name: aws-eks-cluster-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.839142+00:00'
updated_at: '2023-04-10T20:19:58.273833+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/EKS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/eks-cluster-listing]]'
commands:
  - '[[commands/aws-eks-list-clusters]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS EKS Cluster Enumeration

## Summary

This procedure enumerates all Amazon Elastic Kubernetes Service (EKS) clusters in a target AWS account using the AWS CLI. It provides a list of cluster names, enabling attackers to identify potential targets for further exploitation, such as unauthorized access to containerized applications or cluster resources.

## Description

Amazon EKS is a managed Kubernetes service that simplifies deploying and scaling containerized workloads on AWS. Enumerating EKS clusters reveals the infrastructure footprint, allowing attackers to map out high-value targets like production workloads or sensitive data stores. This technique relies on AWS API permissions for EKS and assumes valid credentials are configured in the AWS CLI. It maps to MITRE ATT&CK for cloud service discovery, as it uncovers deployed services without direct interaction. Use this in scenarios where initial AWS access is obtained via compromised credentials or IAM roles, to pivot towards Kubernetes-specific attacks.

## Requirements

1. Valid AWS credentials with at least `eks:ListClusters` permission (e.g., via IAM policy attached to the user/role).
2. AWS CLI version 2.x installed and configured with `aws configure` to set access key, secret key, region, and output format.
3. Network access to AWS APIs (typically over HTTPS port 443).
4. Optional: jq installed for parsing JSON output.

## Defense

- Enforce least privilege by granting EKS list permissions only to necessary roles and monitoring their usage via AWS CloudTrail.
- Enable AWS Organizations SCPs to restrict EKS actions across accounts.
- Set up CloudTrail alerts for `ListClusters` API calls from unusual IPs or roles.
- Use AWS IAM Access Analyzer to detect overly permissive policies.

## Objectives

1. Retrieve a complete list of EKS clusters in the target AWS account.
2. Identify cluster names for subsequent targeting, such as describing clusters or accessing control planes.
3. Validate AWS credentials' scope without triggering more invasive actions.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly set up with credentials that have EKS permissions. This prevents authentication errors during enumeration and confirms the session's validity.

Run the AWS STS get-caller-identity command using [[commands/aws-sts-get-caller-identity]] to verify your identity and permissions:

```bash
aws sts get-caller-identity
```

> This command outputs JSON with Account, UserId, and Arn. If it succeeds without errors, proceed. If credentials are invalid, reconfigure using `aws configure`. Expected: No AccessDenied errors.

### Step 2: List EKS Clusters

**Context**: Execute the core enumeration to fetch all EKS clusters. This step directly queries the EKS service and returns cluster names in JSON format, providing the attack surface overview.

Use the AWS EKS list-clusters command via [[commands/aws-eks-list-clusters]]:

```bash
aws eks list-clusters
```

> The command queries the default region set in your AWS config. To specify a region, add `--region us-east-1`. Expected: JSON response with a "clusters" array listing names like ["cluster-1", "prod-eks"]. If no clusters exist, returns an empty array.

### Step 3: Parse and Review Output

**Context**: Process the JSON output to extract actionable intelligence, such as saving cluster names to a file for further use (e.g., in describe-cluster procedures). This step adds verification and prepares data for chaining attacks.

Pipe the output to jq for filtering using [[commands/aws-eks-list-clusters-with-jq]] (or manually if jq unavailable):

```bash
aws eks list-clusters | jq -r '.clusters[]'
```

> This extracts individual cluster names. Save to a file: `aws eks list-clusters | jq -r '.clusters[]' > eks_clusters.txt`. Expected: Plaintext list of cluster names. Success: Non-empty list indicates discoverable targets; cross-reference with other AWS services for completeness.
