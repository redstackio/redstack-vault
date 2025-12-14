---
tags:
  - account-takeover
  - social-login
  - lateral-movement
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1078.004]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2aeae1e7-6dcd-430e-9e0a-fbc9e84726e4
created_at: '2025-12-14T17:33:24.525Z'
updated_at: '2025-12-14T17:33:24.525Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Achieve Account Takeover via Linked Social Account

## Summary

This procedure finalizes the attack by logging into the victim's Bumble account using the newly linked attacker's social credentials, granting full control over the profile.

## Description

Post-redirect, the verification endpoint links the attacker's social account (e.g., 'Mahmoud Gamal' Gmail) to the victim's Bumble profile. The attacker then initiates a login flow via Google OAuth on Bumble's site, using their credentials. Since the linkage is established, Bumble authenticates the victim session through the attacker's social provider, allowing access to chats, matches, and settings. This results in complete takeover, with potential for data theft or malicious actions.

## Requirements

1. Successful linkage from previous step
2. Attacker's social account credentials
3. Access to Bumble login page

## Defense

Defensive measures and detection strategies:

- Require explicit user consent for social linkages with multi-factor approval
- Audit and revoke suspicious linkages (e.g., via IP/session mismatch)
- Monitor for account activity anomalies post-linkage, like logins from new locations

## Objectives

1. Gain authenticated access to victim's account
2. Verify control through profile actions
3. Exfiltrate or modify sensitive data

## Instructions

### Step 1: Initiate Social Login

**Context**: Use the linked social provider to log in as the victim.

Navigate to Bumble's login page and select 'Login with Google'. Enter the attacker's Gmail credentials.

> Bumble redirects to Google OAuth, which recognizes the linkage and grants access to the victim's profile without additional verification.

### Step 2: Validate Takeover

**Context**: Confirm control by performing actions on the profile.

Once logged in, update the profile bio, view matches, or send messages.

> Expected: Changes reflect on the victim's account; no access errors. Success indicates full takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[T1078.004]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[social-login]]
- [[lateral-movement]]
