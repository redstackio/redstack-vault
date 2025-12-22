---
tags:
  - aws
  - bypass
  - reauth
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:31:42.698Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3cfe22cc-2df0-49e0-a760-88048c754e51
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
---
# Bypass-Re-Authentication-on-AWS-Portal

## Summary

This procedure exploits the vulnerability by accessing AWS resources via the Access Portal without re-authentication, confirming the session expiration bypass.

## Description

Post-timeout, the portal accepts the stale session, enabling unauthorized actions like account switching or app access. This leads to risks such as data exfiltration, configuration changes, or billing manipulation, violating compliance like GDPR/HIPAA.

## Requirements

1. Accessible AWS Access Portal with stale session
2. Target AWS accounts/apps visible in portal
3. Permissions to perform actions (from original session)

## Defense

Defensive measures and detection strategies:

- Implement global session invalidation on timeout
- Use AWS Organizations for scoped access
- Monitor CloudTrail for unauthorized portal actions

## Objectives

1. Gain unauthorized resource access
2. Demonstrate bypass impact
3. Highlight multi-service session risks

## Instructions

### Step 1: Select Account or App

**Context**: Interact with portal to trigger access.

Click on an available AWS account or integrated app.

> Expect seamless redirection to the service without SSO.

### Step 2: Perform Unauthorized Action

**Context**: Validate full access.

E.g., navigate to S3 buckets or EC2 instances and list resources.

> Success if actions complete; observe for any delayed revocation.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Reversible Encryption]] Multi-Factor Authentication Instrument

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[session-hijack]]
- [[unauthorized-access]]
