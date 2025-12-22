---
id: proc-access-endpoints-unifi-329659
tags:
  - web-access
  - vulnerability-probe
  - unifi-video
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.722Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-UniFi-Video-Configuration-Restore-Endpoints

## Summary

This procedure tests and accesses the 'backup' and 'wizard' endpoints in the UniFi Video web interface using a low-privileged session, exploiting the lack of authorization checks to confirm vulnerability to configuration manipulation.

## Description

The UniFi Video web interface on Windows servers exposes 'backup' and 'wizard' endpoints for configuration restore without enforcing privilege checks for PUBLIC_GROUP or CUSTOM_GROUP users. This procedure uses an existing session to send requests to these endpoints, verifying they are reachable and modifiable. It targets the web application layer and assumes prior authentication. Success indicates the endpoints can be abused for further exploitation like config overwrites.

## Requirements

1. Active low-privileged session (from authentication procedure)
2. Knowledge of endpoint URLs (e.g., /backup, /wizard)
3. HTTP client for sending requests

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) on all endpoints
- Log and alert on access to admin endpoints from low-priv sessions
- Regularly audit configuration endpoints for authorization bypasses

## Objectives

1. Confirm endpoint accessibility without admin privileges
2. Identify lack of privilege enforcement
3. Gather response data for crafting malicious payloads

## Instructions

### Step 1: Prepare Session for Requests

**Context**: Load the authenticated session to include cookies in subsequent requests.

Use the saved cookies from login.

### Step 2: Probe 'backup' Endpoint

**Context**: Send a request to the 'backup' endpoint to test access.

Execute a GET request with curl:

```bash
curl -X GET -b cookies.txt https://target-unifi-video/backup
```

> Expected output: Response body or form for backup/restore, without 403 errors, confirming access.

### Step 3: Probe 'wizard' Endpoint

**Context**: Similarly test the 'wizard' endpoint for configuration wizard access.

Execute a GET request with curl:

```bash
curl -X GET -b cookies.txt https://target-unifi-video/wizard
```

> Expected output: Wizard interface or API response accessible to low-priv user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[vulnerability-probe]]
- [[unifi-video]]
