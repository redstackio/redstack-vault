---
id: 574953ed-45fa-4436-8c6e-9f0f4b11b6b8
name: AWS-Account-Identity-Check
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.626346+00:00'
updated_at: '2023-04-10T20:19:48.459605+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - '[[tags/checking-user-identity]]'
  - '[[tags/cloud-aws]]'
  - '[[tags/discovery]]'
commands:
  - '[[commands/get-aws-caller-identity]]'
platforms:
  - AWS
  - Linux
  - macOS
  - Windows
tools: []
validated: true
---

# AWS-Account-Identity-Check

## Summary

The AWS Account Identity Check procedure retrieves details about the AWS account and IAM identity associated with the current credentials using the AWS CLI. This is essential in security assessments to confirm the operator's access level, account ownership, and role assumptions, enabling better reconnaissance and privilege mapping in cloud environments.

## Description

During red team engagements or penetration testing in AWS, operators often need to verify their current identity to understand the scope of access without alerting defenders prematurely. This procedure leverages the AWS Security Token Service (STS) GetCallerIdentity API via the AWS CLI to output the account ID, user ID, and ARN. It helps identify if credentials belong to a user, role, or assumed session, and can reveal misconfigurations like overly permissive roles. The technique aligns with discovery phases where attackers gather system information to plan further actions, such as resource enumeration or lateral movement.

## Requirements

1. AWS CLI version 2 or later installed and properly configured with access keys, secret keys, or temporary credentials via environment variables, config files, or IAM roles.
2. Network access to AWS STS endpoints (typically available in most regions).
3. Permissions to invoke sts:GetCallerIdentity (this action is allowed by default for most IAM policies unless explicitly denied).

## Defense

- Enable and monitor AWS CloudTrail for STS API calls, alerting on unusual GetCallerIdentity invocations from non-standard IP ranges or high-frequency queries.
- Implement IAM policies with least privilege, denying unnecessary STS actions and requiring justification for identity queries.
- Use AWS Config rules to detect and remediate overly broad permissions that allow identity discovery without business need.

## Objectives

1. Retrieve the AWS account ID, IAM user/role ARN, and unique user ID to confirm current access.
2. Validate credential validity and session type (e.g., temporary vs. permanent) for operational planning.
3. Identify potential entry points for privilege escalation by noting the identity's base permissions.

## Instructions

### Step 1: Execute Identity Query

**Context**: Run the AWS CLI command to query the STS service for caller details. This step provides immediate feedback on the active identity and should be performed early in any AWS engagement to baseline access.

**Command** ([[commands/get-aws-caller-identity]]):

```bash
aws sts get-caller-identity
```

> The command sends a request to the STS endpoint and returns a JSON object with identity information. If successful, parse the output to note the Account field for the 12-digit account ID, Arn for the full resource name (e.g., user or role), and UserId for the unique identifier. Errors like 'AccessDenied' indicate insufficient permissions, while 'NoCredentials' suggests configuration issues—troubleshoot by checking ~/.aws/credentials or environment variables.
