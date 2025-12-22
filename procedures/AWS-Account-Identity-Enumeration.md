---
id: 61abeaec-a73b-4449-960b-f6875ca66278
name: AWS-Account-Identity-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.435351+00:00'
updated_at: '2023-04-10T20:20:47.783645+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Exploitation]]'
  - '[[tags/Getting information about the key]]'
  - '[[tags/Privilege Escalation]]'
commands:
  - '[[commands/aws-sts-get-caller-identity]]'
tools:
  - '[[tools/aws-cli]]'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
validated: true
---

# AWS-Account-Identity-Enumeration

## Summary

This procedure retrieves key identity information about the current AWS account, including the account ID, ARN of the calling entity, and user ID, using the AWS Security Token Service (STS). It is a foundational discovery step in cloud penetration testing or red team engagements, enabling attackers to map the environment, verify access levels, and plan subsequent actions like privilege escalation or lateral movement within AWS.

## Description

In AWS environments, understanding the identity of the authenticated principal is essential for reconnaissance. The 'aws sts get-caller-identity' command queries the STS service to return details about the IAM user, role, or assumed role making the request. This information reveals the account structure without requiring elevated privileges, as the sts:GetCallerIdentity action is typically allowed by default. Use this procedure after obtaining initial AWS credentials (e.g., via access keys, IAM roles, or compromised instances) to confirm access and gather metadata for targeted attacks. It maps to MITRE ATT&CK technique T1526, where adversaries discover cloud infrastructure details to facilitate persistence or exfiltration.

## Requirements

1. AWS CLI installed and accessible on the attacker's system.
2. Valid AWS credentials configured (e.g., via environment variables, ~/.aws/credentials file, or IAM role assumption) with permission to call sts:GetCallerIdentity.
3. Network connectivity to AWS STS endpoints (typically over HTTPS on port 443).
4. Basic familiarity with AWS IAM concepts.

## Defense

- Implement least privilege access by restricting sts:GetCallerIdentity to necessary roles, though this is often broad by default; monitor via AWS CloudTrail for anomalous calls.
- Enable AWS CloudTrail logging for STS API actions and integrate with SIEM for alerting on identity queries from unexpected sources.
- Use credential rotation, MFA, and temporary credentials to limit exposure if discovery occurs.
- Regularly audit IAM policies to detect overly permissive access to STS services.

## Objectives

1. Retrieve the AWS account ID to identify the target account.
2. Obtain the ARN and user ID to understand the calling entity's permissions and scope.
3. Validate active credentials and detect any assumed roles for further exploitation planning.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Before executing the identity query, ensure the AWS CLI is properly set up with credentials to avoid authentication errors. This step confirms the environment is ready and prevents common misconfigurations.

Use [[commands/aws-configure-list]] to check current profile settings:

```bash
aws configure list
```

> This command displays the current AWS configuration, including region, output format, and credential source. Expected output includes details like the default region (e.g., us-east-1) and credential file path. If credentials are missing, configure them using `aws configure` with access key ID, secret access key, and default region.

### Step 2: Test Credential Validity

**Context**: Validate that the provided credentials have basic STS access without revealing sensitive information. This acts as a low-risk check before the full identity enumeration.

Execute a simple STS test using [[commands/aws-sts-get-caller-identity]] with output formatting for verification:

```bash
aws sts get-caller-identity --output text
```

> The command returns a tab-separated output with Account, Arn, and UserId if successful. If it fails (e.g., AccessDenied), review IAM policies or credential setup. This step confirms permissions without full JSON parsing.

### Step 3: Perform Full Identity Enumeration

**Context**: Retrieve comprehensive identity details to map the AWS account structure. This is the core action, providing data for subsequent attacks like enumerating resources or escalating privileges.

Run the main enumeration command using [[commands/aws-sts-get-caller-identity]]:

```bash
aws sts get-caller-identity
```

> No additional parameters are needed. The command queries STS and returns a JSON response with Account (12-digit ID), UserId (unique identifier), and Arn (full resource name, e.g., arn:aws:iam::123456789012:user/testuser). Success is indicated by a 200 OK response and valid JSON; errors like InvalidClientTokenId suggest credential issues.
