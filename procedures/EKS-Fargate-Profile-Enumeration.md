---
id: 21842600-6b46-456a-b011-b77cae601795
name: EKS-Fargate-Profile-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.955932+00:00'
updated_at: '2023-04-10T20:20:24.315852+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Application-Access-Token|T1527 - Application Access Token]]'
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud-AWS]]'
  - '[[tags/EKS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Fargate-Profile-Listing]]'
commands:
  - '[[commands/aws-sts-get-caller-identity]]'
  - '[[commands/aws-eks-describe-fargate-profiles]]'
  - '[[commands/jq-extract-fargate-details]]'
platforms:
  - AWS
  - Kubernetes
tools: []
validated: true
---

# EKS Fargate Profile Enumeration

## Summary

The EKS Fargate Profile Enumeration procedure enables the discovery of serverless compute resources in an Amazon EKS cluster by querying Fargate profiles. This reveals critical details such as profile names, pod execution role ARNs, associated subnets, and pod selectors, which can inform attackers about potential privilege escalation paths, network layouts, and workload distributions for subsequent cloud-based attacks.

## Description

In a typical attack scenario, an adversary with compromised AWS credentials (e.g., via IAM role assumption or stolen access keys) uses this procedure during the discovery phase to map the EKS environment. Fargate profiles define how pods are scheduled on AWS Fargate, a serverless compute engine for containers. By enumerating these profiles, attackers identify IAM roles that pods assume, which may have elevated permissions for accessing other AWS services. The procedure leverages the AWS CLI to interact with the EKS API, returning JSON data that can be parsed for actionable intelligence. This is particularly useful in lateral movement within cloud infrastructures, where understanding pod roles can lead to token theft or resource abuse. Prerequisites include valid credentials with the eks:DescribeFargateProfiles permission; without it, the procedure fails with access denied errors.

## Requirements

1. AWS CLI version 2 installed and configured with credentials possessing eks:DescribeFargateProfiles and sts:GetCallerIdentity permissions.
2. Knowledge of the target EKS cluster name.
3. Network connectivity to AWS API endpoints (e.g., eks.us-east-1.amazonaws.com) without restrictive VPC endpoints or proxies blocking access.
4. Optional: jq installed for parsing JSON output.

## Defense

- Implement principle of least privilege by scoping IAM policies to deny eks:DescribeFargateProfiles for non-administrative roles; use AWS Organizations SCPs to enforce this at the account level.
- Enable AWS CloudTrail logging for EKS API calls and monitor for anomalous DescribeFargateProfiles requests via Amazon GuardDuty or custom CloudWatch alarms.
- Rotate IAM credentials regularly and use temporary credentials with short lifetimes; integrate with AWS IAM Access Analyzer to detect overly permissive roles attached to Fargate profiles.
- Segment EKS clusters with network policies and VPC configurations to limit API access from untrusted sources.

## Objectives

1. Verify authenticated access to the AWS account and EKS service.
2. Retrieve comprehensive details on all Fargate profiles in the target cluster.
3. Extract key attributes like pod execution roles and subnets to identify exploitation opportunities.
4. Assess the cluster's serverless footprint for potential lateral movement or persistence.

## Instructions

### Step 1: Verify AWS Credentials and Access

**Context**: Before enumerating Fargate profiles, confirm that the current AWS credentials have the necessary permissions to interact with EKS. This step prevents errors in subsequent commands and provides the caller's identity for attribution in attack planning.

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> This command queries the STS service to return the ARN, account ID, and user ID of the authenticated principal. If the output shows an unexpected role or user (e.g., not the intended compromised credentials), re-authenticate or assume a different role. Success is indicated by a JSON response without errors; failure (e.g., AccessDenied) means insufficient permissions—escalation may be needed.

### Step 2: Enumerate Fargate Profiles

**Context**: Use the AWS CLI to describe all Fargate profiles in the specified EKS cluster. Omitting the --fargate-profile-names parameter retrieves details for every profile, enabling full enumeration. This step gathers raw data on profiles, including ARNs, roles, and subnets.

**Command** ([[commands/aws-eks-describe-fargate-profiles]]):
```bash
aws eks describe-fargate-profiles --cluster-name $_CLUSTER_NAME
```

> Replace $_CLUSTER_NAME with the target EKS cluster name (e.g., my-cluster). The command calls the EKS DescribeFargateProfiles API, returning a JSON object with a 'fargateProfiles' array. Each profile includes fields like fargateProfileName, podExecutionRoleArn, subnets, and selectors (namespace/label rules for pod scheduling). If no profiles exist, the array is empty; errors like ClusterNotFound indicate invalid cluster name or access issues.

### Step 3: Parse and Extract Key Details

**Context**: The raw JSON from the previous step can be voluminous; parse it to focus on high-value information like role ARNs (for potential token abuse) and subnets (for network mapping). This step uses jq to filter and format output for analysis, making it easier to identify targets for further procedures like role assumption.

**Command** ([[commands/jq-extract-fargate-details]]):
```bash
aws eks describe-fargate-profiles --cluster-name $_CLUSTER_NAME | jq '.fargateProfiles[] | {name: .fargateProfileName, roleArn: .podExecutionRoleArn, subnets: .subnets, selectors: .selectors}'
```

> Pipe the describe output into jq for selective extraction. The jq query selects name, roleArn, subnets, and selectors for each profile. Expected output is a streamlined JSON array, e.g., {"name":"fp-default","roleArn":"arn:aws:iam::123:role/eks-fargate","subnets":["subnet-abc"],"selectors":[{"namespace":"default"}]}. If jq is unavailable, save to file and review manually; empty output confirms no profiles or parsing errors.
