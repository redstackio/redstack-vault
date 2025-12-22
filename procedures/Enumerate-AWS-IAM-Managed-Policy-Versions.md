---
id: 0ce1d7f3-0930-4494-a9db-4c9c306d3330
name: Enumerate-AWS-IAM-Managed-Policy-Versions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.317456+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - '[[tags/4. Enumerating Policies]]'
  - '[[tags/Cloud - AWS]]'
  - >-
    [[tags/Listing information about the versions of the specified managed
    policy]]
  - aws-iam
  - policy-enumeration
  - discovery
commands:
  - '[[commands/aws-iam-list-policy-versions]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-IAM-Managed-Policy-Versions

## Summary

This procedure uses the AWS CLI to list all versions of a specified IAM managed policy, allowing attackers to review historical changes in permissions, identify overly permissive versions, or detect misconfigurations that could expose sensitive resources. It is particularly useful in cloud discovery phases to map access controls and plan privilege escalations.

## Description

In an AWS environment, IAM managed policies define permissions for users, groups, and roles. Enumerating policy versions reveals how permissions have evolved, potentially uncovering deprecated weak versions or recent expansions that grant excessive access. Attackers with valid credentials (e.g., via compromised IAM user or assumed role) can invoke the ListPolicyVersions API to retrieve metadata like version IDs, creation dates, and default status. This technique aids in identifying high-value targets, such as policies attached to service roles with S3 or EC2 access, and supports further attacks like policy abuse or lateral movement. The procedure assumes AWS CLI is configured with appropriate credentials and targets a specific policy ARN.

## Requirements

1. Valid AWS credentials with iam:ListPolicyVersions permission (e.g., ReadOnlyAccess or custom policy allowing IAM read actions).
2. AWS CLI installed and configured with access keys or profile (e.g., via `aws configure`).
3. Network access to AWS APIs (no VPC endpoints required for public IAM calls).
4. Knowledge of the target policy ARN (obtainable via prior enumeration like ListPolicies).

## Defense

Defensive measures and detection strategies:

- Implement least privilege: Restrict iam:ListPolicyVersions to administrative roles only and monitor its usage via CloudTrail.
- Enable AWS Config to track policy changes and alert on version creations or modifications.
- Use IAM Access Analyzer to review policy permissions proactively and deny anomalous enumerations via service control policies (SCPs).
- Monitor CloudTrail logs for ListPolicyVersions API calls from unexpected IPs or principals, integrating with SIEM for anomaly detection.

## Objectives

1. Retrieve a complete list of versions for a specified IAM managed policy.
2. Analyze version metadata to identify permission changes or weaknesses.
3. Support broader discovery of AWS access controls for attack planning.

## Instructions

### Step 1: Configure AWS CLI and Identify Policy ARN

**Context**: Before enumerating versions, ensure AWS CLI is set up with credentials that have the necessary IAM read permissions. If the policy ARN is unknown, first enumerate available policies using a separate procedure like List-AWS-IAM-Policies. This step verifies access and prepares the environment.

**Command** ([[commands/aws-iam-list-policies]]):
```bash
aws iam list-policies --scope AWS
```

> This command lists all AWS managed policies. Review the output to select a target policy ARN (e.g., arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess). Expected output includes policy names, ARNs, and descriptions. If access is denied, adjust credentials or assume a role with higher privileges.

### Step 2: List Policy Versions

**Context**: Invoke the ListPolicyVersions API to fetch all versions of the target policy. This reveals historical permissions, helping identify if a non-default version grants broader access that could be exploited.

**Command** ([[commands/aws-iam-list-policy-versions]]):
```bash
aws iam list-policy-versions --policy-arn $_POLICY_ARN
```

> Replace $_POLICY_ARN with the actual ARN (e.g., arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess). This step uses the AWS CLI tool to query IAM. If successful, it returns JSON with version details; parse it to note default versions or recent changes. Decision point: If no versions are returned, the policy may not exist or credentials lack access—fall back to listing policies.
