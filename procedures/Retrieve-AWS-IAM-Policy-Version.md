---
id: 86ca81ec-4402-4695-b933-db5557fe81a6
name: Retrieve-AWS-IAM-Policy-Version
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.882744+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Accessing more credentials]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Persistence & Backdooring]]'
  - '[[tags/Retrieving information about the specified version of the policy]]'
  - aws-iam
  - cloud-discovery
commands:
  - '[[commands/aws-iam-get-policy-version]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Retrieve-AWS-IAM-Policy-Version

## Summary

This procedure retrieves a specific version of an AWS IAM policy using the AWS CLI, allowing attackers with sufficient permissions to inspect policy details, identify misconfigurations, discover assumable roles, and potentially escalate privileges by understanding granted permissions.

## Description

In an AWS environment, IAM policies define permissions for users, groups, and roles. Retrieving a specific policy version provides insight into historical or current permissions, which can reveal overly permissive configurations, backdoor access, or paths to privilege escalation. This technique is useful during cloud discovery and account manipulation phases, where an attacker with initial foothold credentials (e.g., via stolen keys or exploited applications) can enumerate policies attached to roles. The procedure requires IAM permissions like 'iam:GetPolicyVersion' and assumes AWS CLI is configured with valid credentials. Success enables mapping of access rights, identification of exploitable policies, and planning further attacks like role assumption.

## Requirements

1. AWS CLI installed and configured with credentials that have 'iam:GetPolicyVersion', 'iam:ListPolicies', and 'iam:ListPolicyVersions' permissions.
2. Knowledge of the target policy ARN (e.g., obtained via prior enumeration).
3. Network access to AWS APIs (no direct VPC restrictions).
4. Optional: Scriptable environment for automation in red team scenarios.

## Defense

Defensive measures and detection strategies:

- Implement least privilege principles for IAM roles, limiting 'GetPolicyVersion' access to administrative users only.
- Enable AWS CloudTrail for IAM API monitoring; alert on unusual 'GetPolicyVersion' calls from non-administrative roles.
- Use AWS IAM Access Analyzer to review policy permissions and detect anomalous access patterns.
- Rotate credentials regularly and monitor for unauthorized API calls via GuardDuty.

## Objectives

1. Retrieve detailed information about a specific IAM policy version, including the policy document.
2. Identify assumable roles or misconfigurations that enable privilege escalation.
3. Map permissions for further credential access or persistence in the AWS environment.

## Instructions

### Step 1: Identify the Target Policy ARN

**Context**: Before retrieving a version, enumerate available IAM policies to obtain the policy ARN if not already known. This step ensures you target the correct policy.

**Command** ([[commands/aws-iam-list-policies]]):
```bash
aws iam list-policies --scope Local --query 'Policies[?contains(PolicyName, `target-policy-name`)].Arn' --output text
```

> This lists ARNs for local managed policies matching a name pattern. Expected output: A string like 'arn:aws:iam::123456789012:policy/MyPolicy'. If no match, broaden the query or use 'AWS' scope for AWS-managed policies.

### Step 2: List Policy Versions

**Context**: Determine available versions for the policy to select the specific version ID (e.g., 'v1', 'v2'). This helps in targeting non-default versions that might contain legacy misconfigurations.

**Command** ([[commands/aws-iam-list-policy-versions]]):
```bash
aws iam list-policy-versions --policy-arn arn:aws:iam::123456789012:policy/MyPolicy
```

> Outputs a JSON list of versions with IDs and creation dates. Expected output: Array of version objects, e.g., [{'VersionId': 'v2', 'IsDefaultVersion': false}]. Note the desired VersionId.

### Step 3: Retrieve the Specific Policy Version

**Context**: Fetch the policy document and metadata for the chosen version, revealing permissions that can be exploited.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

> This retrieves the policy version details. Expected output: JSON with 'PolicyVersion' including 'Document' (permissions JSON), 'VersionId', and 'IsDefaultVersion'. Review the 'Document' for actions like 'sts:AssumeRole' or broad S3/EC2 access.
