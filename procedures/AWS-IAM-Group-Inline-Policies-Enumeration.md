---
id: 62f3b5d9-da4b-4475-87c8-50720973f7df
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.166554+00:00'
updated_at: '2023-04-10T20:20:11.138213+00:00'
tactics:
  - '[[tactics/Discovery|TA0007]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526]]'
sub_techniques: []
tags:
  - enumerating-groups-iam
  - cloud-aws
  - listing-inline-policies-iam-group
commands:
  - '[[commands/aws-iam-list-group-policies]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
  - Linux
  - Windows
  - macOS
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# AWS-IAM-Group-Inline-Policies-Enumeration

## Summary

This procedure uses the AWS CLI to enumerate the inline policies attached to a specific IAM group, revealing the permissions granted to users within that group. By listing these policies, an attacker can assess access levels, identify overly permissive configurations, and discover potential paths for privilege escalation in an AWS environment.

## Description

AWS Identity and Access Management (IAM) allows grouping users into IAM groups to apply collective policies. Inline policies are embedded directly within a group and define permissions for AWS resources. Enumerating these policies helps map out the group's effective permissions without needing to inspect each user individually. This technique is useful during cloud reconnaissance to understand the attack surface, especially if initial access provides read permissions on IAM resources. It maps to MITRE ATT&CK's Cloud Service Discovery, as it involves querying AWS services to gather configuration details. The procedure assumes access to AWS credentials with the iam:ListGroupPolicies permission and relies on the AWS CLI for execution.

## Requirements

1. Valid AWS credentials (access key and secret key) with at least iam:ListGroupPolicies permission.
2. AWS CLI installed and configured on the attacker's machine.
3. Knowledge of the target IAM group name.
4. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).

## Defense

- Implement least privilege principles by granting only necessary IAM permissions and regularly auditing group policies.
- Enable AWS CloudTrail to log IAM API calls and monitor for unusual enumeration activity, such as repeated ListGroupPolicies requests.
- Use IAM Access Analyzer to identify and alert on unexpected access patterns.
- Enforce multi-factor authentication (MFA) for all IAM users and roles to prevent credential compromise.

## Objectives

1. List all inline policy names attached to the specified IAM group.
2. Analyze the policies to identify permissions that could enable privilege escalation or lateral movement.
3. Gather intelligence on group-level access for further targeting of users or resources.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is installed and configured with credentials that have the required permissions. This step confirms connectivity and authentication before enumeration.

Run the AWS CLI version check and test a basic IAM query to validate access.

**Command** ([[commands/aws-configure-test]]):
```bash
aws sts get-caller-identity
```

> This command returns the account, user, and ARN details if credentials are valid. If it fails with an access denied error, update your credentials or permissions.

### Step 2: Enumerate Inline Policies for the IAM Group

**Context**: Use the AWS IAM API to list the names of inline policies embedded in the target group. This reveals policy names without retrieving the full policy documents, which would require additional permissions.

Replace $_GROUP_NAME with the actual group name (e.g., "Admins" or "Developers").

**Command** ([[commands/aws-iam-list-group-policies]]):
```bash
aws iam list-group-policies --group-name $_GROUP_NAME
```

> The command outputs a JSON response listing policy names. If no policies exist, it returns an empty list. Use the output to identify policies for further inspection with additional commands like get-group-policy if permissions allow.

### Step 3: Analyze Output for Escalation Opportunities

**Context**: Review the listed policy names to determine if they grant excessive permissions, such as admin access or resource creation rights. This manual step helps prioritize follow-up actions.

No specific command is needed here, but pipe the output to jq for parsing if desired:
```bash
aws iam list-group-policies --group-name $_GROUP_NAME | jq '.PolicyNames[]'
```

> Look for policies like "AdminPolicy" or those implying broad access (e.g., containing "*" wildcards when inspected further). Document findings for chaining into privilege escalation procedures.
