---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - authentication
  - initial-access
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-login]]'
verified: false
platforms:
  - Linux
  - Network Switch
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:44.518Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Read-Only-User

## Summary

This procedure establishes a read-only session on the Ubiquiti EdgeSwitch HTTP management interface using valid credentials, serving as the entry point for subsequent exploitation of command injection vulnerabilities.

## Description

In the context of Ubiquiti EdgeSwitch devices running firmware 1.9.0, read-only users can access the web-based management interface but are restricted from executing privileged actions. This procedure uses HTTP POST to the login endpoint to authenticate and retrieve a session cookie, enabling further interactions with the interface. Prerequisites include knowledge of read-only credentials, often obtained through default configurations or phishing. Successful authentication grants limited visibility into device status, setting the stage for injection attacks.

## Requirements

1. Valid read-only username and password for the EdgeSwitch device
2. Network access to the device's HTTP interface (default port 80)
3. curl tool installed on the attacker's machine

## Defense

Defensive measures and detection strategies:

- Enforce strong, unique credentials for all users and disable default accounts
- Implement multi-factor authentication (MFA) on management interfaces
- Monitor login attempts for anomalies using device logs or SIEM tools

## Objectives

1. Obtain a valid session for the HTTP interface
2. Confirm read-only access without triggering alerts
3. Prepare for privilege escalation via injection

## Instructions

### Step 1: Send Login Request

**Context**: Submit credentials to the login endpoint to initiate a session.

**Command** ([[commands/curl-login]]):
```bash
curl -X POST http://<device-ip>/login.cgi -d "username=readonly_user&password=readonly_pass" -c cookies.txt -v
```

> This command sends a POST request with base64-encoded or form-data credentials, storing the session cookie in cookies.txt. Expected output includes a 200 OK or 302 redirect with Set-Cookie header indicating successful authentication.

### Step 2: Verify Session

**Context**: Access a read-only page to confirm session validity.

**Command** ([[commands/curl-session-verify]]):
```bash
curl -b cookies.txt http://<device-ip>/status.cgi -v
```

> Retrieves device status page content. Successful output shows HTML dashboard without login prompt; failure returns 401 Unauthorized.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-login]]
- [[commands/curl-session-verify]]

## Tools Used

- [[tools/curl]]

## Tags

- authentication
- initial-access
