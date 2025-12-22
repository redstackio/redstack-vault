---
id: 8d65ddeb-6c70-4de3-85c7-b1b08db82405
name: AWS-IAM-Policy-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.267207+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/4. Enumerating Policies]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Listing of IAM Policies]]'
  - cloud-aws
  - iam-enumeration
  - discovery
commands:
  - '[[commands/aws-iam-list-all-policies]]'
  - '[[commands/aws-iam-list-attached-policies]]'
  - '[[commands/aws-iam-get-policy-version]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# AWS-IAM-Policy-Enumeration

## Summary

AWS IAM Policy Enumeration is a reconnaissance technique that involves querying an AWS account to list Identity and Access Management (IAM) policies attached to users, groups, and roles. This procedure helps identify overly permissive policies, such as those granting broad access to S3 buckets or EC2 instances, which can reveal paths for privilege escalation or lateral movement within the cloud environment. It is typically used after obtaining initial AWS credentials during cloud penetration testing or red team engagements.

## Description

In AWS environments, IAM policies define permissions for principals like users and roles. Attackers with limited credentials (e.g., read-only access) can enumerate these policies to map the attack surface, spotting misconfigurations like *FullAccess policies or wildcard (*) permissions that allow unauthorized actions. This procedure uses the AWS CLI to query policies without modifying the environment, making it stealthy. It assumes the attacker has credentials with iam:ListPolicies, iam:ListAttachedRolePolicies, and iam:GetPolicyVersion permissions. The output is JSON-formatted, which can be piped to tools like jq for analysis. Common use cases include initial discovery in compromised AWS accounts or during cloud security assessments to validate least-privilege enforcement.

## Requirements

1. Valid AWS credentials configured in the AWS CLI with at least iam:ListPolicies, iam:ListRolePolicies, and iam:GetPolicy permissions.
2. AWS CLI version 2.x installed and accessible via the command line.
3. Network access to the AWS API endpoints (no VPC restrictions blocking IAM calls).
4. Optional: jq installed for parsing JSON output to identify permissive actions.

## Defense

- Implement the principle of least privilege by regularly auditing and minimizing IAM policy permissions using tools like AWS IAM Access Analyzer.
- Enable AWS CloudTrail to log all IAM API calls, including list-policies requests, and set up alerts for anomalous enumeration activity from unexpected IPs or roles.
- Use IAM policy conditions to restrict actions based on source IP, MFA status, or time of day, and enforce service control policies (SCPs) in AWS Organizations to limit discovery capabilities.
- Monitor for unusual API call volumes via Amazon GuardDuty, which can detect reconnaissance patterns in cloud environments.

## Objectives

1. Retrieve a comprehensive list of all IAM policies in the target AWS account to understand permission structures.
2. Filter and identify attached policies to focus on actively used permissions that may enable escalation.
3. Inspect policy details to detect overly permissive statements, such as wildcard resources or administrative actions.

## Instructions

### Step 1: List All IAM Policies

**Context**: Begin by retrieving the full list of IAM policies (both AWS-managed and customer-managed) to get an overview of available permissions in the account. This step establishes the baseline for further analysis without filtering.

**Command** ([[commands/aws-iam-list-all-policies]]):
```bash
aws iam list-policies
```

> The command queries the IAM service for all policies and returns JSON output including policy names, ARNs, descriptions, and attachment counts. Pipe the output to jq (e.g., | jq '.Policies[] | {PolicyName, Arn, AttachmentCount}') for easier reading. This step confirms the attacker's ability to perform discovery and reveals the total number of policies.

### Step 2: List Attached IAM Policies

**Context**: Narrow down to policies that are actively attached to users, groups, or roles, as unattached policies pose less immediate risk. This helps prioritize policies that could be exploited for privilege escalation.

**Command** ([[commands/aws-iam-list-attached-policies]]):
```bash
aws iam list-policies --only-attached
```

> This invocation filters the results to show only policies in use, reducing noise from unused customer policies. The output includes attachment counts greater than zero. Review for policies like "AdministratorAccess" or those with high attachment counts, indicating broad usage. If no policies are attached, it may indicate a misconfigured or empty account.

### Step 3: Retrieve Policy Version Details

**Context**: For any suspicious policies identified in previous steps (e.g., those with wildcard permissions), fetch the full policy document to inspect statements, actions, and resources. This reveals exact permissions like s3:* or ec2:RunInstances.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

> Replace $_POLICY_ARN with the ARN from prior output (e.g., arn:aws:iam::123456789012:policy/MyPolicy) and $_VERSION_ID with the default 'v1' or latest. The response includes the policy document in JSON format. Look for "Effect": "Allow" with broad "Action" or "Resource": "*". This step provides the actionable intelligence for escalation planning.
