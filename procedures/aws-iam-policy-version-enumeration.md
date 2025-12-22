---
id: 733dff2c-6ee8-48e7-b984-5cbf83d47655
name: aws-iam-policy-version-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.763400+00:00'
updated_at: '2023-04-10T20:20:26.792790+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Accessing more credentials]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Listing information about the version of the policy]]'
  - '[[tags/Persistence & Backdooring]]'
commands:
  - '[[commands/aws-iam-list-policy-versions]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS IAM Policy Version Enumeration

## Summary

The AWS IAM Policy Version Enumeration procedure discovers all versions of a specified IAM policy, including their creation dates and default status. This technique is useful for identifying outdated policy versions that may contain excessive permissions or known vulnerabilities, enabling attackers to map access controls and plan further privilege escalation or persistence in an AWS environment.

## Description

In an AWS environment, IAM policies can have multiple versions, with only one set as the default. Enumerating these versions reveals historical changes in permissions, potentially exposing overly permissive configurations from past versions that could be exploited if an attacker gains access to rollback capabilities or references them indirectly. This procedure targets customer-managed policies and requires the 'iam:ListPolicyVersions' permission. It is commonly used during cloud discovery phases to assess the security posture of IAM configurations, identify weak points for lateral movement, or prepare for policy manipulation attacks. The output provides version IDs, which can be used in subsequent actions like attaching or detaching policies.

## Requirements

1. Valid AWS credentials with 'iam:ListPolicyVersions' permission on the target policy.
2. AWS CLI installed and configured with access keys or IAM role.
3. The ARN of the target IAM policy (e.g., obtained via prior enumeration of policies).
4. Network access to AWS API endpoints (no specific ports beyond standard HTTPS).

## Defense

Defensive measures and detection strategies:

- Regularly audit and rotate IAM policies to minimize historical versions; use policy versioning controls to limit retention.
- Implement least-privilege access: Restrict 'iam:ListPolicyVersions' to administrative roles only and monitor its usage via AWS CloudTrail.
- Enable AWS Config rules to detect and alert on policy version changes or excessive permissions in non-default versions.
- Use AWS IAM Access Analyzer to review policy permissions across versions and identify external access risks.

## Objectives

1. Discover all versions of a target IAM policy, including creation dates and default status.
2. Identify potential vulnerabilities such as outdated or overly permissive policy versions.
3. Map permissions granted across policy versions to understand access controls for users or roles.

## Instructions

### Step 1: Prepare the Policy ARN

**Context**: Obtain the ARN of the IAM policy to enumerate. This can be done via prior discovery procedures like listing all policies with 'aws iam list-policies'. The ARN format is 'arn:aws:iam::account-id:policy/policy-name'.

Ensure AWS CLI is authenticated:

```bash
aws sts get-caller-identity
```

> This verifies your current identity and permissions. Expected output includes your account ID, user ARN, and role if assumed.

### Step 2: List Policy Versions

**Context**: Execute the enumeration command to retrieve all versions of the specified policy. This step reveals version details, helping identify non-default versions that might grant unintended access if exploited.

**Command** ([[commands/aws-iam-list-policy-versions]]):

```bash
aws iam list-policy-versions --policy-arn $_POLICY_ARN
```

> Replace $_POLICY_ARN with the actual ARN (e.g., arn:aws:iam::123456789012:policy/MyPolicy). This command queries the AWS IAM API and returns a JSON response listing versions. If the policy has no versions or access is denied, it will error accordingly. Use --output table for human-readable format if needed.

### Step 3: Analyze Output for Vulnerabilities

**Context**: Review the JSON output to check for multiple versions, focusing on creation dates and permissions in older versions. Cross-reference with policy documents using 'aws iam get-policy-version' if needed.

Parse the output (manual or via jq for automation):

```bash
aws iam list-policy-versions --policy-arn $_POLICY_ARN | jq '.Versions[] | {VersionId: .VersionId, CreateDate: .CreateDate, IsDefaultVersion: .IsDefaultVersion}'
```

> Expected output: A list of version objects. Look for non-default versions created long ago, which may indicate unmaintained permissive policies. Success is confirmed by receiving version details without permission errors.
