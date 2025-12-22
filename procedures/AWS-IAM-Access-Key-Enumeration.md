---
id: 34e73b25-7b63-48f9-9123-bfe645b92153
name: AWS-IAM-Access-Key-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.956216+00:00'
updated_at: '2023-04-10T20:20:23.576984+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
  - '[[Credentials in Registry]]'
tags:
  - cloud-aws
  - listing-iam-access-keys
commands:
  - '[[commands/aws-iam-list-access-keys]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-IAM-Access-Key-Enumeration

## Summary

This procedure enumerates all access keys associated with a specified AWS IAM user account using the AWS CLI. It allows attackers or auditors to identify active, inactive, or potentially compromised access keys that could grant programmatic access to AWS resources, enabling further credential access or resource manipulation.

## Description

AWS Identity and Access Management (IAM) controls access to AWS services and resources through users, roles, and access keys. Access keys consist of an Access Key ID and a Secret Access Key, used for API calls and CLI interactions. This procedure lists access keys for a given IAM user, revealing details like key status (Active/Inactive), creation date, and last used date. In an attack scenario, this is used post-initial access to discover credentials for lateral movement or persistence in cloud environments. It targets unsecured credentials stored in IAM configurations, aligning with scenarios where attackers have console or CLI access. Prerequisites include authenticated AWS CLI session with iam:ListAccessKeys permission. Expected outcomes include a JSON list of keys, which can be parsed for further exploitation like key rotation or usage auditing.

## Requirements

1. Valid AWS credentials with iam:ListAccessKeys permission (or broader IAM read access).
2. AWS CLI installed and configured with access keys or SSO.
3. Network access to AWS endpoints (no VPC restrictions blocking IAM API calls).
4. Optional: Specify a user name if not listing for the current authenticated user.

## Defense

- Regularly audit IAM users and access keys using AWS IAM Access Analyzer or CloudTrail logs to detect anomalous listings.
- Implement least privilege: Restrict iam:ListAccessKeys to trusted roles only.
- Enable MFA for IAM users and monitor for CLI/API calls via CloudTrail; alert on access key enumeration from unusual IPs.
- Rotate access keys periodically and deactivate unused ones.

## Objectives

1. Retrieve a complete list of access keys for a target IAM user.
2. Identify active or recently used keys for potential exploitation.
3. Verify key status to assess ongoing access risks.

## Instructions

### Step 1: List Access Keys for IAM User

**Context**: Authenticate to AWS CLI and execute the list command to retrieve access key details. This step assumes AWS CLI is configured; if targeting a specific user, provide the --user-name parameter. The output provides key IDs and metadata without exposing secret keys, but enables further actions like deactivation or usage checks.

**Command** ([[commands/aws-iam-list-access-keys]]):
```bash
aws iam list-access-keys --user-name $_USERNAME
```

> This command queries the IAM service for access keys associated with the specified user. It returns a JSON structure with AccessKeyMetadata entries, including AccessKeyId, Status (Active/Inactive), CreateDate, and LastUsedDate. If no --user-name is provided, it lists keys for the currently authenticated user. Success is indicated by a 200 OK response and non-empty AccessKeyMetadata array. Parse the JSON to identify exploitable keys (e.g., active ones without recent rotation).

### Step 2: Parse and Validate Output

**Context**: Review the JSON output to confirm key details and check for unauthorized or dormant keys. Use jq or similar for filtering if needed, though this is optional for basic enumeration.

**Command** ([[commands/aws-iam-list-access-keys]]):
```bash
aws iam list-access-keys --user-name $_USERNAME | jq '.AccessKeyMetadata[] | {AccessKeyId: .AccessKeyId, Status: .Status, CreateDate: .CreateDate}'
```

> Filters the output to show only relevant fields. Expected output is a list of key objects. If jq is unavailable, manually inspect the JSON. This verifies the enumeration and highlights keys for follow-up actions like testing validity with aws sts get-caller-identity.
