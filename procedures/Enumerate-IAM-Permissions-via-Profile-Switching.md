---
tags:
  - iam
  - permission-enumeration
  - profile-switching
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/export-aws-profile-admin]]'
  - '[[commands/aws-bedrock-agent-list-agents-nonprod-admin]]'
  - '[[commands/export-aws-profile-noperm]]'
  - '[[commands/aws-bedrock-agent-list-agents-nonprod-noperm]]'
  - '[[commands/aws-bedrock-agent-list-agents-nonprod-variant]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:28.788Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d5baa99c-5eae-4544-9de7-6f129c92fada
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Valid Accounts]]'
---
# Enumerate-IAM-Permissions-via-Profile-Switching

## Summary

This procedure uses AWS CLI profiles to switch between privileged and non-privileged IAM roles, testing permissions on non-production Bedrock-Agent endpoints without generating CloudTrail logs for silent enumeration.

## Description

With compromised credentials, adversaries can enumerate IAM permissions by observing API responses (success vs. AccessDenied) on unlogged endpoints. This targets Bedrock-Agent in us-west-2, using profile exports to simulate different access levels. No production data is accessed, but it aids in credential validation and privilege mapping. Requires multiple IAM profiles configured in AWS CLI.

## Requirements

1. AWS CLI with multiple profiles (admin and noperm)
2. Non-production endpoint URLs
3. Basic IAM knowledge for profile setup

## Defense

Defensive measures and detection strategies:

- Rotate credentials regularly and monitor for unusual profile usage
- Implement least-privilege IAM policies and deny non-standard endpoints
- Use AWS IAM Access Analyzer to detect over-permissions

## Objectives

1. Infer permissions from response differences
2. Validate compromised credentials stealthily
3. Confirm multi-endpoint applicability

## Instructions

### Step 1: Switch to Privileged Profile and Test

**Context**: Set admin profile and call endpoint to observe success.

**Command** ([[commands/export-aws-profile-admin]]):
```bash
export AWS_PROFILE=admin
```

**Command** ([[commands/aws-bedrock-agent-list-agents-nonprod-admin]]):
```bash
aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2
```

> Expected output: {"agentSummaries": []}; no log.

### Step 2: Switch to Non-Privileged Profile and Test

**Context**: Set noperm profile and call to observe denial.

**Command** ([[commands/export-aws-profile-noperm]]):
```bash
export AWS_PROFILE=noperm
```

**Command** ([[commands/aws-bedrock-agent-list-agents-nonprod-noperm]]):
```bash
aws bedrock-agent list-agents --endpoint-url [redacted] --region us-west-2
```

> Expected output: AccessDeniedException; no log.

### Step 3: Test Variant Endpoint

**Context**: Confirm on additional non-production variant.

**Command** ([[commands/aws-bedrock-agent-list-agents-nonprod-variant]]):
```bash
aws bedrock-agent list-agents --endpoint-url [redacted]-2 --region us-west-2
```

> Expected output: Success or denial based on profile; no log.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/export-aws-profile-admin]]
- [[commands/aws-bedrock-agent-list-agents-nonprod-admin]]
- [[commands/export-aws-profile-noperm]]
- [[commands/aws-bedrock-agent-list-agents-nonprod-noperm]]
- [[commands/aws-bedrock-agent-list-agents-nonprod-variant]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- iam
- aws
- enumeration
