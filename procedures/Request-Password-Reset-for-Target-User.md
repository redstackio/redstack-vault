---
id: proc-rocket-password-reset
tags:
  - password-reset
  - initial-access
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-password-reset-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.930Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Request-Password-Reset-for-Target-User

## Summary

This procedure initiates a password reset request for a target user in Rocket.Chat using their email address, generating a reset token in the MongoDB database that can be targeted for subsequent injection attacks.

## Description

In the context of exploiting Rocket.Chat, this step requires knowing the target's email and uses the unauthenticated /api/v1/users.forgotPassword endpoint to trigger an email (which may not be sent if email is disabled) and store a temporary reset token. This sets up the blind NoSQL injection in the next phase. Prerequisites include network access to the instance and the Python requests library for API calls.

## Requirements

1. Target Rocket.Chat URL and port (default 3000)
2. Target user's email address
3. HTTP client like Python requests or curl
4. No authentication needed

## Defense

Defensive measures and detection strategies:

- Enable email notifications and monitor for suspicious reset requests
- Implement rate limiting on forgot password endpoints
- Log all pre-auth API calls for anomaly detection

## Objectives

1. Generate a database-stored reset token for the target
2. Prepare for token extraction via injection
3. Maintain unauthenticated access throughout

## Instructions

### Step 1: Send Password Reset Request

**Context**: Use an HTTP POST to the forgotPassword endpoint with the target's email to create the token.

**Command** ([[commands/curl-password-reset-request]]):
```bash
curl -X POST 'http://target:3000/api/v1/users.forgotPassword' -H 'Content-Type: application/json' -d '{"user":{"email":"target@example.com"}}'
```

> This sends the request; expect a JSON success response like {"success": true}. The token is now in MongoDB, queryable via getPasswordPolicy.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-password-reset-request]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]

## Tags

- password-reset
- initial-access
