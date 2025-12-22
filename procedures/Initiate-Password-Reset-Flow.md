---
tags:
  - password-reset
  - api
  - initial-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-initiate-password-reset]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: cc551179-31a6-4bf6-974f-d6254bc0fc85
created_at: '2025-12-14T17:33:12.400Z'
updated_at: '2025-12-14T17:33:12.400Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Password-Reset-Flow

## Summary

This procedure starts the password reset process on helpdesk.bistudio.com by sending a request to generate a 6-digit SMS token for a target staff username, exploiting the lack of protections in the API endpoint.

## Description

In the context of account takeover, this step triggers the backend to send an SMS to the victim's phone without requiring authentication. The endpoint /api/system/verification-codes accepts a POST with the username and generates the token. Responses can be intercepted if errors occur, but initiation typically succeeds. This is part of a larger chain where the token is then bruteforced.

## Requirements

1. Network access to https://helpdesk.bistudio.com
2. Target username (e.g., 'admin')
3. Tools like curl or Burp Suite for requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on reset initiation endpoints
- Enforce ReCAPTCHA on all reset flows
- Log and monitor SMS token generations by IP

## Objectives

1. Generate and send SMS token to target
2. Confirm flow initiation without blocks
3. Prepare for token bruteforce

## Instructions

### Step 1: Send Initiation Request

**Context**: POST to the verification endpoint with the target username to trigger SMS.

**Command** ([[commands/post-initiate-password-reset]]):
```bash
curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes -H "Content-Type: application/json" -d '{"username":"admin"}'
```

> This sends the JSON payload and expects a response indicating the token was sent. If an error occurs (e.g., invalid username), intercept and modify in Burp Suite.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/post-initiate-password-reset]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[password-reset]]
- [[api]]
- [[initial-access]]
