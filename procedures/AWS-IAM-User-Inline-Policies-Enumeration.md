---
id: c1d206ae-038d-4990-8cdc-74b8ddf8cd5f
name: AWS-IAM-User-Inline-Policies-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.089333+00:00'
updated_at: '2023-04-10T20:20:04.453431+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques:
  - '[[sub-techniques/Domain Groups|T1069.002 - Domain Groups]]'
tags:
  - '[[tags/1. Enumerating IAM users]]'
  - '[[tags/Cloud - AWS]]'
  - >-
    [[tags/Listing the names of the inline policies embedded in the specified
    IAM user]]
commands:
  - '[[commands/AWS-IAM-List-User-Policies]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
validated: true
---

# AWS-IAM-User-Inline-Policies-Enumeration

## Summary

This procedure enumerates the inline policies attached to a specific IAM user in an AWS environment, providing insight into the user's permissions and potential privilege escalation paths. By listing these policies, an attacker can identify overly permissive configurations that allow actions like resource access or further enumeration.

## Description

In AWS Identity and Access Management (IAM), inline policies are embedded directly into a user, group, or role and are not reusable like managed policies. This procedure uses the AWS CLI to query the IAM service for the names of inline policies associated with a target user. It requires credentials with the iam:ListUserPolicies permission and helps in mapping out permission boundaries during discovery phases of an attack. The output is a JSON list of policy names, which can be used to fetch policy details in subsequent steps. This technique is particularly useful in cloud environments where understanding user privileges is key to lateral movement or persistence.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., via `aws configure`).
2. The credentials must have the `iam:ListUserPolicies` permission for the target user.
3. Network access to the AWS API endpoints (no specific ports beyond standard HTTPS/443).
4. Knowledge of the target IAM username.

## Defense

- Implement least privilege principles by regularly auditing and refining IAM policies to remove unnecessary inline policies.
- Enable AWS CloudTrail logging for IAM API calls to detect enumeration attempts.
- Use IAM Access Analyzer to identify and alert on anomalous permission grants.
- Enforce multi-factor authentication (MFA) and monitor for unauthorized credential usage.

## Objectives

1. List the names of inline policies attached to a specified IAM user.
2. Identify potential permission weaknesses for further exploitation.
3. Gather data for chaining with other IAM enumeration procedures.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Before enumerating policies, ensure your AWS CLI is set up with credentials that can access IAM details for the target user. This step prevents errors due to insufficient permissions or misconfiguration.

Run `aws sts get-caller-identity` to confirm your identity and permissions:

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> This command verifies your current AWS identity. If it fails with an access denied error, update your credentials or IAM role.

### Step 2: Enumerate Inline Policies for the Target User

**Context**: Use the AWS IAM API to retrieve the list of inline policy names for the specified user. This reveals custom permissions embedded in the user account, which may grant elevated access to AWS resources.

**Command** ([[commands/AWS-IAM-List-User-Policies]]):
```bash
aws iam list-user-policies --user-name $_USER_NAME
```

> Replace $_USER_NAME with the target IAM username (e.g., `john.doe`). The command queries the IAM service and returns a JSON response with policy names. If no inline policies exist, the list will be empty. Use the output policy names to fetch full policy documents with `aws iam get-user-policy` in a follow-up procedure.

**Expected Output**:
```json
{
    "PolicyNames": [
        "AdminAccessPolicy",
        "S3ReadOnlyPolicy"
    ]
}
```

This indicates the user has two inline policies that can be further investigated.
