---
id: proc-uuid-2
tags:
  - account-switching
  - lateral-movement
  - twitter-ads
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.674Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Switch to Attacker Account

## Summary

This procedure logs out of the victim Twitter Ads account and authenticates into a separate attacker account, maintaining the Burp proxy to prepare for request modification in the exploitation phase.

## Description

To demonstrate the IDOR, the attacker must operate from a different account without access to the victim's data. This step ensures session isolation while keeping interception active. The attacker account must also have Ads & Analytics enabled. Expected outcome: Clean transition to the attacker dashboard.

## Requirements

1. Valid credentials for the attacker Twitter Ads account
2. Burp Suite proxy still active from previous steps
3. No shared sessions between accounts

## Defense

Defensive measures and detection strategies:

- Session management to prevent rapid logins/logouts across accounts
- IP-based anomaly detection for frequent account switches
- Audit logs for authentication events

## Objectives

1. Securely log out of the victim account
2. Authenticate into the attacker account
3. Verify Ads dashboard access

## Instructions

### Step 1: Log Out of Victim Account

**Context**: End the current session to avoid conflicts.

No specific command; use the logout button in the Twitter dashboard.

> Navigate to account settings and select logout. Clear any cached sessions in the browser if needed.

### Step 2: Authenticate into Attacker Account

**Context**: Log in with attacker credentials while proxying through Burp.

No specific command; enter credentials at ads.twitter.com.

> Ensure proxy is on, log in, and confirm access to https://ads.twitter.com/accounts/<attacker_account_id>/audience_manager.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-switch
- authentication
