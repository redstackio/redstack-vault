---
id: bypass-auth-cisco-sx80-default
tags:
  - auth-bypass
  - default-credentials
  - cisco
  - telepresence
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Hardware
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:31:31.080Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
---
# Bypass Authentication with Default Credentials on Cisco SX80

## Summary

This procedure exploits unchanged default credentials on the Cisco TelePresence SX80 web interface to bypass authentication and gain initial administrative access, common in misconfigured video conferencing deployments.

## Description

Cisco TelePresence SX80 devices ship with default usernames and passwords (e.g., admin / blank or cisco / cisco per documentation) that, if not altered, allow unauthenticated attackers with network access to log in via the HTTPS management portal. This leads to user-level access that can escalate. Target environment: Exposed SX80 on port 443. Outcomes: Dashboard access for further configuration manipulation.

## Requirements

1. Network reachability to the SX80 web interface (https://<IP>)
2. Knowledge of default credentials (e.g., `█████████` / ████)
3. Web browser or HTTP client for login

## Defense

Defensive measures and detection strategies:

- Enforce credential changes on device provisioning
- Enable multi-factor authentication if supported
- Log and alert on failed/successful logins from unknown IPs

## Objectives

1. Authenticate without custom credentials
2. Access the user dashboard as ███
3. Enable escalation to full admin control

## Instructions

### Step 1: Access Web Interface

**Context**: Navigate to the login portal of the SX80.

Open https://███████ in a browser.

> The login form appears; no command needed, direct GUI interaction.

### Step 2: Submit Default Credentials

**Context**: Enter known defaults to bypass auth.

Input username `█████████` and password ████, then submit.

> Success grants access as user ███, displaying the management interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Default Accounts]] Default Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[default-credentials]]
