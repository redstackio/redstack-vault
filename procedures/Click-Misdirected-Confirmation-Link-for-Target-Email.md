---
tags:
  - shopify
  - confirmation-bypass
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 308f5936-52a1-49b3-8743-0b515eeb255a
created_at: '2025-12-13T09:01:26.836Z'
updated_at: '2025-12-13T09:01:26.836Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Click Misdirected Confirmation Link for Target Email

## Summary

This procedure confirms the target email by clicking the misdirected link, bypassing proper verification.

## Description

Activating the link associates the account with the target's email without their knowledge.

## Requirements

1. Confirmation link from email
2. Web browser

## Defense

Defensive measures and detection strategies:

- Implement token-based confirmation with expiration
- Log and alert on confirmation from unexpected IPs

## Objectives

1. Verify the new email
2. Update account ownership

## Instructions

### Step 1: Activate Link

**Context**: Use the link to confirm.

Access the link in the email to update the account email to the target's email.

> Confirmation page should indicate success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- confirmation-bypass
