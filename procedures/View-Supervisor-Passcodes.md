---
id: proc-mtn-view-passcodes-001
tags:
  - credential-access
  - passcode-exposure
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.292Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# View Supervisor Passcodes

## Summary

This procedure retrieves sensitive passcodes for supervisor accounts via an admin dashboard endpoint, exposing credentials for potential account takeover.

## Description

The supervisor passcode endpoint (/admin/supervisors/passcodes) is accessible without additional protections, listing passcodes in plain text. This facilitates further compromise in the MTN Group web app's supervisory layer.

## Requirements

1. Admin session with dashboard access
2. Passcode endpoint URL
3. HTTP GET capability

## Defense

Defensive measures and detection strategies:

- Hash or encrypt passcodes in storage and transit
- Restrict passcode views to authorized roles only
- Alert on access to sensitive credential endpoints

## Objectives

1. Retrieve supervisor passcode list
2. Expose credentials for escalation
3. Enable unauthorized supervisor access

## Instructions

### Step 1: Access Passcode Endpoint

**Context**: GET the passcodes to view them.

Example:

```bash
curl -X GET https://target-app.com/admin/supervisors/passcodes \
  -H "Authorization: Bearer <session_token>"
```

> Expected output: JSON with supervisor IDs and plain-text passcodes.

### Step 2: Extract and Use Passcodes

**Context**: Parse the response for usable credentials.

No command; manually note passcodes for login attempts.

> Success if passcodes match and enable supervisor logins.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-access]]
- [[passcode-exposure]]
