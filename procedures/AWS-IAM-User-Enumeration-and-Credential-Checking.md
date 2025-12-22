---
id: 8d633a6e-77ad-42da-9579-f8f57def9004
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.983289+00:00'
updated_at: '2024-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/1. Enumerating IAM users]]'
  - '[[tags/Checking credentials for the user]]'
  - '[[tags/Cloud - AWS]]'
  - aws-cli
  - iam
commands:
  - '[[commands/aws-iam-list-users]]'
  - '[[commands/aws-sts-get-caller-identity]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-IAM-User-Enumeration-and-Credential-Checking

## Summary

This procedure outlines the steps to enumerate IAM users within an AWS environment and validate the current credentials using AWS CLI. It allows an attacker to identify account users and confirm the access level of stolen or compromised credentials, facilitating further discovery and potential privilege escalation in cloud environments.

## Description

In AWS, IAM manages user access to resources. Enumerating users reveals the structure of the account, including usernames and creation dates, which can guide targeted attacks. Validating credentials via the STS service confirms the identity and account details associated with the access keys. This technique is commonly used after obtaining initial AWS credentials through phishing, misconfigurations, or other means. The procedure assumes AWS CLI is set up and relies on API permissions; if the credentials lack IAM read access, enumeration may fail, indicating limited privileges.

## Requirements

1. AWS CLI v2 installed on a Linux/macOS/Windows system.
2. Valid AWS access key ID and secret access key configured via `aws configure`.
3. Network connectivity to AWS endpoints (no VPC restrictions blocking API calls).
4. Permissions: `iam:ListUsers` for enumeration; `sts:GetCallerIdentity` (usually allowed by default).

## Defense

Defensive measures and detection strategies:

- Enforce least privilege by denying `iam:ListUsers` to non-admin roles via IAM policies.
- Enable MFA for all IAM users and require it for sensitive actions.
- Monitor AWS CloudTrail logs for `ListUsers` and `GetCallerIdentity` API calls, alerting on unusual sources or frequencies.
- Use AWS Organizations SCPs to restrict IAM actions across accounts.
- Implement credential rotation and anomaly detection with AWS GuardDuty.

## Objectives

1. Enumerate IAM users within an AWS environment to map account structure.
2. Check the credentials of the current session to verify access and identity.
3. Identify opportunities to access sensitive data or escalate privileges within the AWS environment.

## Instructions

### Step 1: Enumerate IAM Users

**Context**: Query the IAM service to list all users in the account. This step discovers potential targets for credential attacks or privilege checks. If permissions are insufficient, the command will error with an AccessDenied, indicating the credential's limitations.

**Command** ([[commands/aws-iam-list-users]]):

```bash
aws iam list-users --output table
```

> This retrieves a table-formatted list of IAM users, including ARNs and creation dates. Use the output to note admin-like users for further targeting. Why: Provides visibility into the user base without needing web console access.

### Step 2: Validate Current Credentials

**Context**: Retrieve the ARN, account ID, and user ID of the current caller to confirm credential validity and scope. This verifies if the keys are active and reveals the effective identity for planning next moves.

**Command** ([[commands/aws-sts-get-caller-identity]]):

```bash
aws sts get-caller-identity
```

> Outputs JSON with UserId, Account, and Arn. Cross-reference with enumerated users to understand the current position. Why: Ensures the session is authenticated and provides context for access testing; no additional permissions beyond STS are needed.
