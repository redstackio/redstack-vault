---
id: proc-verify-impersonation-001
name: Verify Successful Authentication as Victim
tags:
  - verification
  - takeover
  - post-exploitation
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.679Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify Successful Authentication as Victim

## Summary

This procedure confirms the authentication bypass by inspecting the response and performing actions under the victim's session, validating full account control including modifications and data access.

## Description

Post-request, the 200 OK response contains victim-specific data (e.g., ID, name), indicating success. Further validation involves using the session to query account details or execute destructive actions like deletions. This step highlights the vulnerability's severity, allowing large-scale leaks in affected systems like the reported 100,000-user base.

## Requirements

1. Successful response from modified login
2. Session cookies or tokens from the response
3. Access to victim-specific endpoints

## Defense

Defensive measures and detection strategies:

- Session binding to original login IP/user-agent
- Real-time alerts on account access from anomalous sources
- Regular audits of login parameter logs

## Objectives

1. Parse response for victim account confirmation
2. Test account actions to ensure takeover
3. Document impact for reporting

## Instructions

### Step 1: Inspect Response

**Context**: Analyze the server's reply in Burp.

In Burp Repeater, view the response body.

> Look for 200 OK with JSON like {"success":true,"user":{"id":456,"name":"Victim","type":"premium"}}—no password field required.

### Step 2: Test Account Access

**Context**: Use the session to perform actions.

Forward to the app dashboard or use cookies in browser.

> Attempt profile view, password change, or account deletion; success without victim credentials confirms takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[verification]]
- [[account-takeover]]
