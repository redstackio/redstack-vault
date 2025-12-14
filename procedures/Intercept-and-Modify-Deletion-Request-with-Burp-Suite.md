---
id: proc-uuid-2
tags:
  - idor
  - burp-suite
  - api-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.195Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Deletion-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept a legitimate account deletion request from the Firefox Accounts API, analyze its structure, and modify the JSON payload to target a victim's email, exploiting the IDOR vulnerability.

## Description

The Firefox Accounts API endpoint /v1/account/destroy accepts a JSON payload with an 'email' field for SSO accounts without passwords, but fails to verify session ownership. By intercepting via Burp Suite's Proxy and Repeater, the attacker can substitute the email, allowing deletion of any account. This targets web-based REST APIs and requires an active authenticated session.

## Requirements

1. Burp Suite installed and configured as browser proxy
2. Active attacker session via SSO login
3. Knowledge of victim's email address

## Defense

Defensive measures and detection strategies:

- Validate session user ID matches the targeted email in API logic
- Require authPW or additional tokens for deletion requests
- Log and alert on mismatched session-email pairs in requests

## Objectives

1. Capture and understand the deletion request format
2. Tamper with the payload to enable arbitrary targeting
3. Prepare a valid exploitable request without triggering defenses

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception to capture API traffic from the browser.

In Burp Suite, enable Intercept in the Proxy tab, configure browser proxy to 127.0.0.1:8080, and log in to Firefox Accounts.

### Step 2: Trigger and Intercept Deletion

**Context**: Initiate a self-deletion to capture the request structure.

Navigate to account deletion in the UI, submit, and intercept the POST to https://api.accounts.firefox.com/v1/account/destroy in Burp. Forward to Repeater and cancel the UI action.

### Step 3: Analyze and Modify Payload

**Context**: Edit the JSON to substitute the victim's email.

In Repeater, view the request body (e.g., {"email": "attacker@example.com"}), change to {"email": "victims344@gmail.com"}, and ensure headers include session cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[tools/Burp-Suite]]
- [[api-interception]]
