---
id: proc-transfer-cookie-takeover
tags:
  - account-takeover
  - session-hijacking
  - web
  - php
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:34.351Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Transfer-Cookie-and-Perform-Account-Takeover

## Summary

This procedure transfers the stolen PHPSESSID cookie to the main site, enabling unauthorized access to user information and password updates for full account takeover.

## Description

By injecting the PHPSESSID from the alternate site into the main domain's cookie store, attackers bypass authentication due to shared sessions. This IDOR variant allows viewing sensitive data and modifying account details in PHP web apps. Critical impact includes complete control over the victim's Starbucks account.

## Requirements

1. Valid PHPSESSID cookie from alternate site
2. Browser session on main site (card.starbucks.com.sg)
3. Knowledge of account management endpoints

## Defense

Defensive measures and detection strategies:

- Bind sessions to specific domains/IPs
- Implement multi-factor authentication for sensitive actions
- Detect cookie manipulation via client-side integrity checks

## Objectives

1. Authenticate on main site using stolen cookie
2. Access and view user information
3. Update password to secure persistent access

## Instructions

### Step 1: Inject Cookie into Main Site

**Context**: Set the PHPSESSID in the browser's cookie storage for the main domain.

Open developer tools on card.starbucks.com.sg, go to Application > Cookies, and add/edit PHPSESSID with the stolen value. Set domain and path appropriately.

> Refresh the page to apply the session.

### Step 2: Access Account and Update Password

**Context**: Use the hijacked session to perform unauthorized actions.

Navigate to user profile or settings. View information, then proceed to password change form and submit a new password.

> Confirm takeover by logging out and back in with new credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[session-hijacking]]
