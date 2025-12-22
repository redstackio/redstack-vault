---
tags:
  - credential-capture
  - phishing
  - google-app
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - Google
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
updated_at: '2025-12-14T17:28:12.907Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6dee40c3-f31e-4839-ae10-605a67a17322
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
---
# Capture-Credentials-via-Malicious-Google-App

## Summary

This procedure uses a pre-created malicious Google app to intercept credentials during the forced relogin prompted by the SetSID redirect, harvesting thousands of accounts in the wild.

## Description

The malicious app, registered with Google, acts as an intermediary during relogin, capturing username and password before redirecting to getmorefollowers.biz. This relies on the lack of app legitimacy checks and victim unawareness.

## Requirements

1. Malicious Google app registered with OAuth scopes for authentication
2. SetSID URL pointing to the app's endpoint
3. Victim entering credentials on the fake login page

## Defense

Defensive measures and detection strategies:

- Review and revoke unknown Google apps in account settings
- Use multi-factor authentication to mitigate credential theft
- Detect phishing via URL mismatches (e.g., non-official domains)

## Objectives

1. Intercept Google username and password
2. Store credentials for attacker use
3. Redirect to next stage without alerting victim

## Instructions

### Step 1: Intercept During Relogin

**Context**: Victim enters creds on the app's login interface.

The app captures input via form submission to attacker's server.

> Expected: Credentials logged; silent redirect.

### Step 2: Redirect Post-Capture

**Context**: After capture, forward to getmorefollowers.biz.

Implement redirect in app logic.

> Expected: Victim sees follower site, unaware of theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-capture]]
- [[Phishing]]
- [[google-app]]
