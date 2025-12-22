---
type: procedure
description: >-
  This procedure enumerates all IAM policies associated with an AWS account and
  optionally retrieves detailed information about a specific policy.
verified: true
submitted: true
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Groups]]'
sub_techniques: []
tags:
  - AWS
  - Cloud
  - IAM
  - Discovery
commands:
  - '[[commands/aws-iam-list-policies]]'
  - '[[commands/aws-iam-get-policy]]'
platforms:
  - Cloud
tools:
  - '[[tools/aws-cli]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# List-IAM-Policies-in-AWS-Account

## Summary

This procedure allows security testers or administrators to list all Identity and Access Management (IAM) policies in an AWS account, providing visibility into the permissions and access controls defined. It is useful for reconnaissance, auditing, or compliance checks in cloud environments, helping identify overly permissive policies or misconfigurations that could lead to privilege escalation.

## Description

IAM policies in AWS define permissions for users, groups, and roles. Listing them reveals the scope of access granted across the account, such as read/write permissions to S3 buckets, EC2 instances, or other services. This procedure uses the AWS CLI to query the IAM service, which requires appropriate credentials (e.g., via access keys or IAM role assumption). It targets AWS accounts and assumes the executing user has at least the iam:ListPolicies permission. In an offensive security context, this can map out the attack surface for further exploitation, such as identifying service-linked roles or customer-managed policies. The optional description step provides JSON details on policy documents, including statements and conditions.

## Requirements

1. AWS CLI installed and configured with credentials that have iam:ListPolicies and iam:GetPolicy permissions.
2. Access to the target AWS account (e.g., via compromised keys or assumed role).
3. Network connectivity to AWS endpoints (no VPC restrictions blocking IAM API calls).

## Defense

- Enable AWS CloudTrail to log IAM API calls like ListPolicies and GetPolicy for anomaly detection.
- Implement least-privilege access: Restrict iam:ListPolicies to trusted roles only using IAM policies.
- Monitor for unusual IAM queries via AWS GuardDuty or custom CloudWatch alarms on API activity.

## Objectives

1. Enumerate all IAM policies to understand account permissions landscape.
2. Optionally retrieve details of a specific policy for deeper analysis.
3. Identify potential misconfigurations for privilege escalation paths.

## Instructions

### Step 1: List All IAM Policies

**Context**: This step queries the AWS IAM service to retrieve a list of all policies (both AWS-managed and customer-managed) in the account. It provides policy ARNs, names, descriptions, and types, allowing identification of key permissions without needing elevated privileges beyond read access.

**Command** ([[commands/aws-iam-list-policies]]):
```bash
aws iam list-policies
```

> This command returns a JSON array of policies. Review the output for policy names like "AdministratorAccess" or custom ones that grant broad permissions. If the account has many policies, paginate using --max-items or --marker if truncated.

### Step 2: Describe a Specific IAM Policy

**Context**: After identifying a policy of interest from Step 1, use its ARN to fetch detailed information, including the policy document with permission statements. This helps analyze exact permissions, such as Allow effects on resources, which could reveal exploitable access patterns.

**Command** ([[commands/aws-iam-get-policy]]):
```bash
aws iam get-policy --policy-arn $_POLICY_ARN
```

> Replace $_POLICY_ARN with the full ARN (e.g., arn:aws:iam::123456789012:policy/MyCustomPolicy). The output includes policy version, attachment count, and a link to the policy document. Success is indicated by a 200 OK response with policy details; errors occur if the ARN is invalid or access is denied.
