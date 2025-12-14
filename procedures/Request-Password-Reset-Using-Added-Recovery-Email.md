---
tags:
  - password-reset
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-password-reset]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:23.470Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 070df4a7-088e-4eb1-b601-3a5ee11ec755
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-Password-Reset-Using-Added-Recovery-Email

## Summary

This procedure initiates a password reset for the victim's account, routing the link to the attacker's added recovery email.

## Description

After IDOR manipulation, the site's reset flow sends links to recovery emails. This step leverages the injected email to receive the reset token without victim's knowledge.

## Requirements

1. Victim's username
2. Access to attacker's email (now recovery for victim)
3. Site's password reset endpoint

## Defense

Defensive measures and detection strategies:

- Notify users of recovery email additions
- Require secondary verification for resets
- Monitor reset frequency per account

## Objectives

1. Trigger reset link delivery to attacker
2. Bypass primary email notifications
3. Prepare for final takeover

## Instructions

### Step 1: Initiate Reset

**Context**: Use the site's forgot password form with victim's username.

Submit the reset request.

### Step 2: Receive and Confirm Link

**Context**: Check attacker's email for the reset link.

Execute [[commands/curl-password-reset]] to simulate if API-based:

```bash
curl -X POST https://target-site.com/forgot-password \
  -d "userName=victim_username" \
  -s
```

> Link arrives in attacker's inbox (e.g., containing reset token).

**Expected Output**: Email with clickable reset link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-password-reset]]

## Tools Used


## Tags

- password-reset
- account-takeover
