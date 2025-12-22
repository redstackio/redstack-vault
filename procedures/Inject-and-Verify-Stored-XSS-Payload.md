---
tags:
  - xss
  - stored-xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8e0a5c6d-642a-4ad2-b31a-16dbf9f8f865
created_at: '2025-12-11T03:47:59.461Z'
updated_at: '2025-12-11T03:47:59.461Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Inject and Verify Stored XSS Payload

## Summary

This procedure injects an XSS payload via the poisoned cache and verifies its execution on the target page.

## Description

Building on the cached redirect, host an XSS payload on the attacker domain to render malicious JavaScript when users access the sign-in page, interfering with page integrity. This achieves stored XSS without backend impact.

## Requirements

1. Successful cache poisoning from previous steps
2. Web server to host XSS payload
3. Browser or curl for verification

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP)
- Monitor for unexpected scripts in cached responses

## Objectives

1. Inject executable JavaScript payload
2. Verify rendering on legitimate user access
3. Demonstrate page integrity compromise

## Instructions

### Step 1: Host XSS Payload

**Context**: Set up payload on attacker.com.

Host a page with: <script>alert('XSS')</script>

### Step 2: Verify Execution

**Context**: Access the poisoned page to trigger XSS.

**Command** ([[commands/curl-http-smuggling]]):
```bash
curl https://paypal.com/signin
```

> Check if the response includes the injected script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

## Commands Used

- [[commands/curl-http-smuggling]]

## Tools Used

- [[tools/cURL]]

## Tags

- #xss
- #stored-xss
