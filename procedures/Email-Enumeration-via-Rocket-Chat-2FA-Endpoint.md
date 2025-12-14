---
tags:
  - information-disclosure
  - email-enumeration
  - rocket-chat
  - api
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-rocket-chat-valid-email-enumeration]]'
  - '[[commands/curl-rocket-chat-invalid-email-enumeration]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:31:19.143Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4866d886-ed85-48ba-9f52-cfa7bebfc173
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Email-Enumeration-via-Rocket-Chat-2FA-Endpoint

## Summary

This procedure exploits an information disclosure vulnerability in Rocket.Chat's /api/v1/users.2fa.sendEmailCode endpoint to enumerate valid email addresses without authentication. By sending POST requests with the emailOrUsername parameter, attackers can distinguish valid users (200 OK success) from invalid ones (400 Bad Request error), enabling the harvesting of registered emails for further attacks.

## Description

The vulnerability arises because the API provides different responses based on user existence: valid emails trigger a successful 2FA code send response, while invalid ones return an explicit error. This leak allows unauthenticated attackers to confirm email registrations systematically. The target environment is a Rocket.Chat web application, typically on port 3000. Prerequisites include network access to the endpoint; no login is required. Expected outcomes include a list of valid emails, which can facilitate brute-force password attacks, phishing, or credential stuffing.

## Requirements

1. Network access to the Rocket.Chat instance (e.g., http://target:3000)
2. HTTP client like curl for sending POST requests
3. List of potential email addresses to test

## Defense

Defensive measures and detection strategies:

- Implement consistent error responses (e.g., always return 200 with generic messages) to avoid information leaks
- Rate-limit API endpoints to prevent enumeration attempts
- Monitor logs for repeated requests to /api/v1/users.2fa.sendEmailCode from unknown IPs
- Enable authentication requirements for sensitive endpoints

## Objectives

1. Confirm existence of specific email addresses in the Rocket.Chat user base
2. Build a list of valid emails for targeted attacks
3. Demonstrate the information disclosure without triggering alerts

## Instructions

### Step 1: Test with a Valid Email

**Context**: Send a POST request to the endpoint using a known or suspected valid email to observe the success response, confirming the vulnerability.

**Command** ([[commands/curl-rocket-chat-valid-email-enumeration]]):
```bash
curl -X POST http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -d '{"emailOrUsername":"test@test.test"}'
```

> This command sends a JSON payload with an existing email. Expected output is HTTP 200 OK with {"success":true}, indicating the email is registered and a 2FA code would be sent.

### Step 2: Test with an Invalid Email

**Context**: Send a POST request with a non-existent email to observe the error response, establishing the baseline for differentiation.

**Command** ([[commands/curl-rocket-chat-invalid-email-enumeration]]):
```bash
curl -X POST http://rocket-chat.local:3000/api/v1/users.2fa.sendEmailCode -H "Content-Type: application/json" -d '{"emailOrUsername":"test2@test.test"}'
```

> This command uses a fabricated email. Expected output is HTTP 400 Bad Request with {"success":false,"error":"Invalid user [error-invalid-user]","errorType":"error-invalid-user"}, confirming the email does not exist.

### Step 3: Automate Enumeration

**Context**: Script the process to test multiple emails, logging responses to identify valid ones.

**Instructions**: Use a loop in bash or a tool like Burp Intruder to iterate over an email list, parsing responses for 200 OK to flag valid entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-rocket-chat-valid-email-enumeration]]
- [[commands/curl-rocket-chat-invalid-email-enumeration]]

## Tools Used


## Tags

- information-disclosure
- email-enumeration
- rocket-chat
- api
