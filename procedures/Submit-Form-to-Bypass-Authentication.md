---
tags:
  - form-submission
  - exploit-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.925Z'
sub_techniques: []
id: 66332184-fb4c-4437-93d1-fb891b28ff1f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Form-to-Bypass-Authentication

## Summary

This procedure triggers the SQL injection by submitting the form, executing the payload to bypass authentication and retrieve another user's scholarship status if birth dates match.

## Description

Clicking 'Check Status' sends the POST request with the injected SSN and birth date to the backend, where unsanitized inputs lead to query manipulation. Success grants access to sensitive data; failure may require birth date iteration.

## Requirements

1. Payload and birth date entered
2. Form submittable

## Defense

Defensive measures and detection strategies:

- Audit logs for successful logins without valid SSN
- Anomaly detection on birth date/SSN pairs

## Objectives

1. Execute injection for auth bypass
2. Exfiltrate user data
3. Validate vulnerability impact

## Instructions

### Step 1: Click Submit

**Context**: Submit the tampered form to the server.

Browser action:

```plaintext
Click 'Check Status' button
```

> Observe response: If successful, displays scholarship status of a matching user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[form-submission]]
- [[exploit-trigger]]
