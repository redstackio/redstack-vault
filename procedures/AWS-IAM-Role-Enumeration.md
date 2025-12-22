---
id: 9ef18a7b-a6d1-4cce-bab3-b499f01227e2
name: AWS-IAM-Role-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.807214+00:00'
updated_at: '2023-04-10T20:19:56.865374+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - exploitation-scenario
  - accessing-credentials
  - cloud-aws
  - listing-iam-roles
  - persistence
commands:
  - '[[commands/aws-iam-list-roles]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# AWS-IAM-Role-Enumeration

## Summary

This procedure enumerates all IAM roles in an AWS account using the AWS CLI, providing visibility into role names, ARNs, and creation dates. It is useful for attackers to identify roles with potentially elevated permissions for privilege escalation or lateral movement in cloud environments.

## Description

In AWS environments, IAM roles define permissions for services, users, or applications. Enumerating these roles reveals the structure of access controls, allowing an attacker with initial credentials to map out high-privilege roles for further exploitation, such as assuming roles via STS or targeting misconfigured trust policies. This technique aligns with discovery phases in cloud attacks, where understanding resource permissions enables persistence and escalation. The procedure assumes access to the AWS CLI configured with valid credentials (e.g., access key and secret key) and targets the default AWS region unless specified otherwise. Expected outcomes include a JSON list of roles, which can be parsed to filter for admin-like roles (e.g., those with 'admin' in the name or attached to critical policies).

## Requirements

1. Valid AWS credentials with at least read access to IAM (e.g., `iam:ListRoles` permission).
2. AWS CLI installed and configured (via `aws configure` with access key, secret key, and default region).
3. Network access to AWS endpoints (no VPC restrictions blocking IAM API calls).
4. Optional: jq for parsing JSON output if filtering is needed post-execution.

## Defense

- Implement least privilege by limiting `iam:ListRoles` to administrative users only.
- Enable AWS CloudTrail logging for IAM API calls to detect enumeration attempts.
- Use IAM Access Analyzer to review and restrict role trust policies.
- Monitor for unusual credential usage patterns via AWS GuardDuty or SIEM integration.

## Objectives

1. Retrieve a complete list of IAM roles in the target AWS account.
2. Identify roles with elevated or sensitive permissions for potential targeting.
3. Support further actions like role assumption or policy attachment analysis.

## Instructions

### Step 1: Execute IAM Role Listing

**Context**: This step uses the AWS CLI to query the IAM service and list all roles. No additional arguments are required for the basic enumeration, but the output provides essential details like role names and ARNs, which can be used to assess permissions manually or via scripting.

**Command** ([[commands/aws-iam-list-roles]]):
```bash
aws iam list-roles
```

> This command sends a request to the IAM API and returns a JSON structure containing an array of roles. Each role entry includes the role name, ARN, creation date, and description if available. Success is indicated by a 200 OK response with the 'Roles' array populated. If no roles exist, the array will be empty. Pipe the output to jq for filtering, e.g., `aws iam list-roles | jq '.Roles[] | {RoleName, Arn}'` to extract names and ARNs only. Review the output for roles like 'AdminRole' or those created recently, which may indicate recent configurations.
