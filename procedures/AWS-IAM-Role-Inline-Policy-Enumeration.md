---
id: f953efd8-0251-4135-a694-477660aaf389
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.243186+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Application-Access-Token|T1527 - Application Access Token]]'
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - Enumerating-Roles
  - Cloud-AWS
  - IAM-Inline-Policy-Enumeration
commands:
  - '[[commands/aws-iam-list-role-policies]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
validated: true
---

# AWS-IAM-Role-Inline-Policy-Enumeration

## Summary

This procedure enumerates the names of inline policies embedded directly within a specified AWS IAM role using the AWS CLI. Inline policies are JSON documents that define permissions and are attached exclusively to the role they are embedded in, allowing attackers with compromised credentials to discover associated permissions for potential privilege escalation or lateral movement in cloud environments.

## Description

In AWS Identity and Access Management (IAM), roles provide temporary permissions for AWS services and entities to access resources. Inline policies are embedded directly in the role's JSON definition, unlike managed policies which are standalone. This procedure uses the ListRolePolicies API via the AWS CLI to retrieve the names of these inline policies for a given role, revealing the scope of permissions without needing to fetch the full policy details. This discovery technique helps identify over-privileged roles in scenarios where an attacker has assumed a role or obtained credentials with list permissions. It applies to AWS environments where IAM roles are used, such as EC2 instances or cross-account access, and can chain into further enumeration or exploitation if sensitive permissions like S3 access or EC2 control are uncovered.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with permissions to call the `iam:ListRolePolicies` API action on the target role.
2. AWS CLI installed and configured with the appropriate profile or default credentials (e.g., via `aws configure`).
3. Network access to AWS endpoints (no VPC endpoints required for IAM, but ensure no restrictive security groups block outbound HTTPS to IAM).
4. Knowledge of the target IAM role name, obtained from prior enumeration like listing roles via `aws iam list-roles`.

## Defense

- Apply the principle of least privilege by reviewing and minimizing inline policies in IAM roles, preferring managed policies for reusability and auditing.
- Enable and monitor AWS CloudTrail logs for `ListRolePolicies` API calls, setting up CloudWatch alarms for unusual IAM activity from unexpected sources or roles.
- Implement AWS Organizations SCPs (Service Control Policies) to restrict IAM actions across accounts and enforce MFA for privileged roles.
- Use AWS IAM Access Analyzer to identify and alert on external access or unused permissions in roles.

## Objectives

1. Retrieve the list of inline policy names associated with a specific IAM role.
2. Understand the permission structure of the role to identify potential escalation paths or sensitive access.
3. Support further cloud discovery by chaining to policy content retrieval or role assumption techniques.

## Instructions

### Step 1: List Inline Policies for the Target Role

**Context**: This step queries the AWS IAM service to enumerate the names of all inline policies attached to the specified role. The command outputs a JSON response listing policy names, which can be parsed to identify permissions like S3 bucket access or EC2 instance control. Ensure your AWS CLI is authenticated with credentials that have `iam:ListRolePolicies` permission; if denied, it indicates insufficient access and may require privilege escalation first.

**Command** ([[commands/aws-iam-list-role-policies]]):
```bash
aws iam list-role-policies --role-name $_ROLE_NAME
```

> This command sends a request to the IAM ListRolePolicies API, where `$_ROLE_NAME` is replaced with the actual role name (e.g., 'MyEC2Role'). The response is a JSON object containing a 'PolicyNames' array. If no inline policies exist, the array will be empty. Pipe the output to `jq` for easier parsing if needed (e.g., `| jq '.PolicyNames[]'`). Success is indicated by HTTP 200 and a non-error response; errors like 'AccessDenied' suggest permission issues.
