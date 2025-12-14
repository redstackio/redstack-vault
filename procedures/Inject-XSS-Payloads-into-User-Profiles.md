---
tags:
  - xss
  - payload-injection
  - user-profile
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1e86dbf0-b374-45eb-b42a-7344efa2a5a2
created_at: '2025-12-13T23:52:55.563Z'
updated_at: '2025-12-13T23:52:55.563Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payloads-into-User-Profiles

## Summary

This procedure involves creating user accounts and stores on a target platform like Shopify, embedding XSS payloads such as XSS Hunter scripts or simple JavaScript in profile fields to exploit lack of input sanitization for later DOM-based execution.

## Description

In the context of Shopify's Device Manager, attackers register test accounts (e.g., using email aliases) and create stores, injecting payloads into names or profiles. These payloads remain dormant until rendered unsanitized in the admin dashboard, enabling JavaScript execution. Prerequisites include access to registration endpoints; no authentication is needed for injection, but the vulnerability relies on admin interaction.

## Requirements

1. Access to user registration and store creation endpoints
2. XSS Hunter account for advanced payload tracking
3. Test email aliases to avoid rate limits (e.g., 'samudra+lp@wearehackerone.com')

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for all user-supplied data
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous account creations with script-like content in profiles

## Objectives

1. Persist malicious payloads in user data for later exploitation
2. Prepare for DOM-based XSS without immediate detection
3. Enable data exfiltration upon admin interaction

## Instructions

### Step 1: Prepare XSS Payloads

**Context**: Select and customize payloads for injection; use XSS Hunter for tracking or a basic alert for testing.

No specific command; manually craft payloads like the XSS Hunter script (obtained from XSS Hunter dashboard) or `<img src=x onerror=prompt(document.domain)>`.

> Embed the payload in account name or profile during registration.

### Step 2: Create Injected Accounts

**Context**: Register accounts and stores with payloads in vulnerable fields.

Navigate to Shopify registration and create an account with email 'samudra+lp@wearehackerone.com', embedding the payload in the name field. Similarly, create a store named 'uji150' with the payload in profile details.

> Successful registration confirms payload storage; verify by logging in and checking profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss]]
- [[payload-injection]]
