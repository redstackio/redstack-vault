---
id: 69758664-7766-4ad2-a8b1-cd62527e7c5c
name: aws-iam-enumerate-attached-role-policies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.219518+00:00'
updated_at: '2023-04-10T20:19:47.011470+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - aws
  - iam
  - role-enumeration
  - discovery
  - cloud
commands:
  - '[[commands/aws-iam-list-attached-role-policies]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# aws-iam-enumerate-attached-role-policies

## Summary

This procedure enumerates all managed policies attached to a specific IAM role in an AWS environment using the AWS CLI. It allows an attacker with valid credentials to discover the permissions associated with the role, potentially revealing over-privileged access points for lateral movement or privilege escalation within the cloud infrastructure.

## Description

In an AWS attack scenario, after obtaining initial credentials (e.g., via reconnaissance or credential dumping), an attacker can use this procedure to map out IAM role permissions. By listing attached policies, the attacker identifies actions the role can perform, such as accessing S3 buckets, EC2 instances, or other services. This discovery technique targets the IAM service and requires the 'iam:ListAttachedRolePolicies' permission on the enumerated role. The output provides policy names, ARNs, and attachment dates, which can be further investigated to chain into exploitation of misconfigurations like excessive S3 read/write access.

## Requirements

1. AWS CLI installed and configured with valid credentials that have at least 'iam:ListAttachedRolePolicies' permission for the target role.
2. Network access to AWS APIs (typically over HTTPS on port 443).
3. Knowledge of the target IAM role name, obtained via prior enumeration (e.g., listing roles with 'aws iam list-roles').

## Defense

Defensive measures and detection strategies:

- Implement least privilege by regularly auditing and minimizing permissions in IAM role policies.
- Enable AWS CloudTrail logging for IAM API calls and monitor for unusual 'ListAttachedRolePolicies' invocations using AWS GuardDuty or SIEM tools.
- Use IAM Access Analyzer to identify and alert on external access or unused permissions.
- Enforce MFA for IAM users and roles, and restrict API access via VPC endpoints or IP allowlists.

## Objectives

1. Gather detailed information on permissions granted to a specific IAM role.
2. Identify potential attack paths, such as roles with broad S3 or EC2 access, for further exploitation.
3. Map the AWS environment's access controls to support targeted privilege escalation or data exfiltration.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is set up with credentials that can access IAM services. This step confirms authentication before enumeration to avoid permission errors.

If not already configured, set up credentials using environment variables or the AWS config file. Test with a basic IAM call like 'aws sts get-caller-identity' to verify access.

> Expected: Successful response showing the caller's ARN and account details. If denied, update credentials or assume a role with sufficient permissions.

### Step 2: List Attached Role Policies

**Context**: Execute the core enumeration command to retrieve all managed policies attached to the specified IAM role. This reveals the policy names and ARNs for further analysis.

**Command** ([[commands/aws-iam-list-attached-role-policies]]):
```bash
aws iam list-attached-role-policies --role-name $_ROLE_NAME
```

> This command queries the IAM service for policies linked to the role. Replace $_ROLE_NAME with the target role (e.g., 'MyEC2Role'). If the role has no attached policies, the response will be an empty array. Pipe the output to jq for parsing if needed: 'aws iam list-attached-role-policies --role-name $_ROLE_NAME | jq ".AttachedPolicies[] | .PolicyName"'.

### Step 3: Analyze Output for Permissions

**Context**: Review the command output to identify high-risk policies. This step involves manual or scripted inspection to determine exploitable permissions, such as 's3:*' or 'ec2:RunInstances'.

Fetch detailed policy documents for each attached policy using 'aws iam get-policy-version' or 'aws iam get-role-policy' for inline policies. For example:
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id v1
```

> Expected: Policy document in JSON format showing allowed actions, resources, and conditions. Look for overly permissive statements (e.g., wildcards on resources) to prioritize attack paths. Document findings for chaining into procedures like S3 bucket enumeration.
