---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - cookie-injection
  - dos
  - web
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.759Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Cookies

## Summary

This core procedure exploits the lack of validation in the api.tumblr.com/console/auth endpoint by injecting arbitrary cookie values via GET parameters, setting invalid oa-consumer_key and oa_consumer_secret cookies with excessive expiration to cause DoS.

## Description

The attack targets the OAuth authorization flow where consumer_key and consumer_secret parameters directly influence cookie setting without sanitization, allowing attribute injection like domain and Max-Age. In a browser context, visiting a crafted URL modifies cookies for the tumblr.com domain. Prerequisites: Authenticated session and created app. Expected outcome: Malformed cookies persist, blocking future API auth until manual deletion.

## Requirements

1. Active Tumblr session with created OAuth app.
2. Web browser supporting cookie manipulation.
3. No pre-existing OAuth cookies.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all cookie-setting parameters.
- Check for existing cookies before overwriting.
- Implement secure cookie flags (HttpOnly, Secure).
- Monitor for anomalous Max-Age values in logs.

## Objectives

1. Inject invalid values into OAuth cookies.
2. Set excessive expiration to persist DoS.
3. Force manual cookie cleanup for recovery.

## Instructions

### Step 1: Craft Malicious URL

**Context**: Prepare the exploit URL targeting the vulnerable endpoint.

Construct: https://api.tumblr.com/console/auth?consumer_key=x;%20domain=tumblr.com;%20Max-Age=1000000000000000000000&consumer_secret=x;%20domain=tumblr.com;%20Max-Age=1000000000000000000000

> URL encodes cookie injection payload.

### Step 2: Visit URL in Browser

**Context**: Trigger cookie modification by loading the URL.

Paste and visit the URL in the authenticated browser session.

> Page may load blank or with error; check dev tools for cookie changes.

### Step 3: Verify Injection

**Context**: Confirm cookies are set as intended.

In dev tools > Application > Cookies > https://www.tumblr.com, inspect oa-consumer_key and oa_consumer_secret.

> Values: 'x', Domain: tumblr.com, Max-Age: 1000000000000000000000.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cookie-injection
- dos
- web

