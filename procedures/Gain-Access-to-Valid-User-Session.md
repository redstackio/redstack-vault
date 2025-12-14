---
tags:
  - session-hijacking
  - valid-accounts
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.994Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a3d370d6-737e-4d66-9af0-654fe8254a77
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Gain Access to Valid User Session

## Summary

This procedure outlines obtaining a valid session cookie for a Phabricator user account, enabling authenticated actions without credentials, serving as the entry point for account manipulation attacks.

## Description

In the context of Phabricator, attackers exploit session persistence or hijacking to impersonate users. This targets web sessions with long expiration times, allowing access to sensitive features like account settings. Prerequisites include proximity to the victim or network interception capabilities. Expected outcome is full session control, bypassing login.

## Requirements

1. Network access to the Phabricator instance or victim's device
2. Tools for cookie interception (e.g., proxy or malware)
3. Knowledge of session cookie names (e.g., phabricator_session)

## Defense

Defensive measures and detection strategies:

- Implement short session timeouts and automatic logout
- Monitor for anomalous session activity from unusual IPs
- Enforce HTTPS and HttpOnly/Secure flags on cookies

## Objectives

1. Acquire active user session
2. Enable subsequent authenticated actions
3. Achieve initial access without credentials

## Instructions

### Step 1: Intercept or Extract Session Cookie

**Context**: Use network tools or physical access to capture the session cookie from a logged-in browser.

**Instructions**: If via MITM, set up a proxy to capture traffic; for physical access, export cookies from browser dev tools (Application > Cookies).

> Locate the Phabricator session cookie and import it into your browser to hijack the session.

### Step 2: Validate Session Access

**Context**: Confirm the session grants access to protected areas.

**Instructions**: Load the Phabricator dashboard or settings page to verify no login redirect occurs.

> Successful load indicates valid session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-hijacking]]
- [[phabricator]]
