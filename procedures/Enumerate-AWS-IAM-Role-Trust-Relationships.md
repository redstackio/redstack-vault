---
id: 97998e8b-1451-4bb2-95a3-37a00c86f790
name: Enumerate-AWS-IAM-Role-Trust-Relationships
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.831987+00:00'
updated_at: '2023-04-10T20:20:40.333958+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Accessing more credentials]]'
  - '[[tags/Cloud - AWS]]'
  - >-
    [[tags/Listing trust relationship between role and user (Which roles we can
    assume)]]
  - '[[tags/Persistence & Backdooring]]'
commands:
  - '[[commands/aws-iam-list-roles]]'
  - '[[commands/aws-iam-get-role]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-IAM-Role-Trust-Relationships

## Summary

This procedure enumerates AWS IAM roles and their trust relationships to identify which roles the current user or principal can assume, enabling discovery of potential privilege escalation paths to higher-privilege roles and access to sensitive resources.

## Description

In AWS environments, IAM roles define trust relationships via policies that specify which entities (users, services, or other roles) can assume them. This procedure uses AWS CLI to list all IAM roles in the account and retrieve their trust policies, allowing an attacker with initial IAM permissions to map assumable roles. This is particularly useful in compromised AWS environments where the attacker has limited credentials, as assuming a higher-privilege role can lead to broader access like S3 buckets, EC2 instances, or further API calls. The technique leverages the ListRoles and GetRole APIs, which require iam:ListRoles and iam:GetRole permissions. Analysis of the AssumeRolePolicyDocument in the output reveals trusted principals, such as ARNs matching the attacker's identity.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) configured via AWS CLI (e.g., using `aws configure`).
2. IAM permissions: iam:ListRoles to list roles and iam:GetRole to retrieve role details.
3. AWS CLI installed and access to the target AWS account/region.
4. Optional: jq for parsing JSON output to filter trust policies.

## Defense

- Regularly audit IAM roles and trust policies using AWS IAM Access Analyzer to identify overly permissive trusts.
- Implement least privilege by scoping trust policies to specific conditions (e.g., external IDs, MFA).
- Enable AWS CloudTrail to log IAM API calls like ListRoles and GetRole for anomaly detection.
- Use IAM roles with temporary credentials and monitor for unusual AssumeRole attempts.

## Objectives

1. List all IAM roles in the AWS account.
2. Retrieve and analyze trust policies to identify assumable roles.
3. Identify high-value roles for potential privilege escalation.

## Instructions

### Step 1: List All IAM Roles

**Context**: Begin by listing all IAM roles in the account to obtain a comprehensive inventory. This step uses the ListRoles API to fetch role names and ARNs, providing the foundation for targeted enumeration. Without this, you cannot systematically check trust relationships.

**Command** ([[commands/aws-iam-list-roles]]):
```bash
aws iam list-roles
```

> This command queries the IAM service and returns a JSON array of roles. Review the output for role names of interest, such as those with admin-like titles (e.g., AdminRole, EC2Access). If the account has many roles, pipe to jq for filtering: `aws iam list-roles | jq '.Roles[].RoleName'`. Success is indicated by a non-empty Roles array; errors occur if permissions are insufficient.

### Step 2: Retrieve Specific Role Trust Policy

**Context**: For each identified role, fetch detailed information including the trust policy to determine if the current principal can assume it. This reveals the AssumeRolePolicyDocument, which specifies trusted entities. Iterate over roles from Step 1, substituting the role name.

**Command** ([[commands/aws-iam-get-role]]):
```bash
aws iam get-role --role-name $_ROLE_NAME
```

> Replace $_ROLE_NAME with a role from Step 1 (e.g., "AdminRole"). The output is a JSON object with Role. AssumeRolePolicyDocument containing the trust policy. Parse it to check if your principal's ARN is listed under "Principal". For example, use jq: `aws iam get-role --role-name AdminRole | jq '.Role.AssumeRolePolicyDocument.Statement[] | select(.Principal.AWS == "*" or contains(your-arn))'`. If the trust allows assumption, proceed to assume the role via `aws sts assume-role`. Success is a 200 OK response with role details; failure indicates insufficient permissions or invalid role name.
