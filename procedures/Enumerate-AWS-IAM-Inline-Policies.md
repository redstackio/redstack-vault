---
id: 306c8cbe-b073-485a-94c9-2647fb004cbf
name: Enumerate-AWS-IAM-Inline-Policies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.371713+00:00'
updated_at: '2023-04-10T20:20:04.805438+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Discovery]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Application Access Token]]'
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - iam-enumeration
  - aws-cloud
  - policy-discovery
commands:
  - '[[commands/aws-iam-get-user-policy]]'
  - '[[commands/aws-iam-get-group-policy]]'
  - '[[commands/aws-iam-get-role-policy]]'
platforms:
  - AWS
tools: []
validated: true
---

# Enumerate-AWS-IAM-Inline-Policies

## Summary

This procedure retrieves inline policy documents attached to AWS IAM users, groups, or roles using AWS CLI commands. It allows attackers with compromised credentials to enumerate permissions, identify overly permissive policies, and discover potential privilege escalation paths within an AWS environment.

## Description

AWS IAM inline policies are embedded directly into users, groups, or roles and define specific permissions for AWS resources. Enumerating these policies reveals the exact actions allowed, such as access to S3 buckets, EC2 instances, or administrative functions. This technique is useful during cloud reconnaissance and lateral movement phases, where an attacker analyzes policy documents to map access rights and plan escalations, like assuming roles with higher privileges. The procedure assumes access to AWS CLI configured with credentials that have at least iam:GetUserPolicy, iam:GetGroupPolicy, or iam:GetRolePolicy permissions. It targets AWS environments and helps in understanding the principle of least privilege violations.

## Requirements

1. AWS CLI installed and configured with access keys or assumed role credentials that permit reading IAM policies (e.g., iam:GetUserPolicy permission).
2. Knowledge of target IAM user names, group names, or role names (can be obtained via prior enumeration like aws iam list-users).
3. Network access to AWS APIs (no specific ports, as it uses HTTPS to api.iam.amazonaws.com).

## Defense

- Regularly audit IAM policies using AWS IAM Access Analyzer to detect overly permissive inline policies.
- Implement least privilege by avoiding inline policies and using managed policies instead; monitor policy changes via CloudTrail.
- Enable MFA for IAM users and use IAM roles with short-lived credentials to limit exposure.
- Set up CloudTrail logging for IAM API calls and alert on get-policy operations from unusual sources.

## Objectives

1. Retrieve inline policy documents for specified IAM users, groups, or roles.
2. Analyze policy contents to identify permissions for privilege escalation or resource access.
3. Map discovered permissions to potential attack paths in the AWS environment.

## Instructions

### Step 1: Identify Targets for Enumeration

**Context**: Before retrieving policies, list available IAM entities to select targets. This step uses separate list commands but provides context for policy enumeration.

Use aws iam list-users, list-groups, or list-roles to gather names (not detailed here, as they are prerequisite procedures).

> Expected: JSON output listing entity names, e.g., {"Users": [{"UserName": "target-user"}]}.

### Step 2: Enumerate User Inline Policy

**Context**: Retrieve the inline policy for a specific IAM user to inspect permissions granted directly to that user account.

**Command** ([[commands/aws-iam-get-user-policy]]):
```bash
aws iam get-user-policy --user-name $_USER_NAME --policy-name $_POLICY_NAME
```

> This command fetches the policy document in JSON format. Replace $_USER_NAME with the target user (e.g., "john.doe") and $_POLICY_NAME with the policy name (e.g., "AdminAccess"). If the policy exists, it returns the policy ARN, document, and creation/update timestamps. Analyze the "PolicyDocument" for "Statement" arrays detailing allowed actions like "s3:*".

### Step 3: Enumerate Group Inline Policy

**Context**: Retrieve the inline policy for a specific IAM group to understand shared permissions among group members, which could affect multiple users.

**Command** ([[commands/aws-iam-get-group-policy]]):
```bash
aws iam get-group-policy --group-name $_GROUP_NAME --policy-name $_POLICY_NAME
```

> Similar to user policy retrieval, this outputs the group's policy document. Use it when targeting groups for broader impact assessment. Expected JSON includes permissions that propagate to group users.

### Step 4: Enumerate Role Inline Policy

**Context**: Retrieve the inline policy for a specific IAM role, useful for identifying assumable roles with elevated privileges in cross-account or service scenarios.

**Command** ([[commands/aws-iam-get-role-policy]]):
```bash
aws iam get-role-policy --role-name $_ROLE_NAME --policy-name $_POLICY_NAME
```

> This command returns the role's inline policy, highlighting trust policies and actions like "sts:AssumeRole". Review for escalation opportunities, such as roles allowing access to sensitive resources.

### Step 5: Analyze Retrieved Policies

**Context**: Parse the JSON outputs manually or with jq to extract actionable permissions.

Use a tool like jq for filtering:
```bash
aws iam get-user-policy --user-name $_USER_NAME --policy-name $_POLICY_NAME | jq '.PolicyDocument.Statement[] | .Action'
```

> Expected: List of allowed actions, e.g., ["ec2:DescribeInstances", "s3:GetObject"]. Look for wildcards (*) or admin-level permissions indicating escalation potential.
