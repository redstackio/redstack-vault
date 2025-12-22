---
id: 6db0fa7a-ac9b-454e-a2d8-697348551947
name: AWS-EKS-Cluster-Information-Gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.863024+00:00'
updated_at: '2023-04-10T20:19:58.930036+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/EKS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing information about a specific cluster]]'
commands:
  - '[[commands/aws-eks-describe-cluster]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-EKS-Cluster-Information-Gathering

## Summary

This procedure retrieves detailed information about a specific Amazon EKS (Elastic Kubernetes Service) cluster using the AWS CLI. It is useful for attackers or security testers to map out the target's cloud infrastructure, identify cluster configurations, versions, and endpoints that could reveal potential attack surfaces or misconfigurations in a Kubernetes environment hosted on AWS.

## Description

In a cloud penetration test or red team engagement, discovering details about EKS clusters helps understand the target's container orchestration setup. The procedure queries the AWS EKS API to fetch metadata such as the cluster name, Kubernetes version, VPC configuration, subnet IDs, security group associations, and the API server endpoint. This information can inform further actions like attempting to access the Kubernetes API, enumerating nodes, or identifying networking exposures. Technically, it leverages the AWS SDK under the hood via the CLI to make a DescribeCluster API call. Prerequisites include authenticated AWS credentials with at least the 'eks:DescribeCluster' permission. The procedure assumes the attacker has compromised or obtained valid AWS IAM credentials with EKS read access.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with permissions to call 'eks:DescribeCluster' on the target cluster.
2. AWS CLI installed and configured with the appropriate profile (e.g., via 'aws configure').
3. Network connectivity to AWS API endpoints (typically over HTTPS on port 443).
4. Knowledge of the target EKS cluster name, which may be obtained from prior enumeration like listing clusters with 'aws eks list-clusters'.

## Defense

- Implement least-privilege IAM policies to restrict 'eks:DescribeCluster' access only to necessary roles and users.
- Enable AWS CloudTrail logging for EKS API calls to monitor and alert on unauthorized DescribeCluster requests.
- Use AWS Organizations SCPs to deny EKS actions in sensitive environments.
- Regularly audit IAM credentials and rotate them to limit exposure from compromised accounts.

## Objectives

1. Retrieve comprehensive metadata about a target EKS cluster to map the cloud infrastructure.
2. Identify potential vulnerabilities such as outdated Kubernetes versions or exposed endpoints.
3. Gather insights for planning subsequent attacks, like node enumeration or API access attempts.

## Instructions

### Step 1: Query EKS Cluster Details

**Context**: Use the AWS CLI to invoke the DescribeCluster operation, specifying the target cluster name. This step assumes you have the cluster name from prior discovery (e.g., via listing clusters). The command returns a JSON response with cluster attributes, which can be parsed for key details like the endpoint URL for further interaction.

**Command** ([[commands/aws-eks-describe-cluster]]):
```bash
aws eks describe-cluster --name $_CLUSTER_NAME
```

> This command makes an API request to the EKS service. Replace $_CLUSTER_NAME with the actual cluster identifier (e.g., 'my-production-cluster'). If successful, it outputs a JSON structure under 'cluster' key containing fields like 'name', 'version', 'endpoint', 'resourcesVpcConfig' (with subnet and security group IDs), 'status', and 'roleArn'. Pipe the output to 'jq' for easier parsing, e.g., 'aws eks describe-cluster --name $_CLUSTER_NAME | jq .cluster'. If the cluster name is invalid or permissions are insufficient, it returns an error like 'ClusterNotFoundException' or 'AccessDeniedException'.
