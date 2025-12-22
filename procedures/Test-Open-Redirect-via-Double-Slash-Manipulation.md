---
tags:
  - open-redirect
  - phishing
  - web-vulnerability
  - cwe-601
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-url-with-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.379Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 06dcff35-e56c-4300-af8b-df39bc1b615c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Open Redirect via Double Slash Manipulation

## Summary

This procedure tests for an open redirect vulnerability in web applications by appending a double slash (//) followed by an arbitrary domain to the base URL, exploiting improper parsing to trigger a 301 redirect without scheme validation. It is primarily used to identify sites vulnerable to phishing redirection.

## Description

In the Skyliner web application on skyliner.io and qa.skyliner.io, the vulnerability arises from inadequate URL validation, allowing attackers to craft requests like https://skyliner.io//blackfan.ru/, which results in a redirect to //blackfan.ru. This protocol-relative redirect bypasses controls, enabling redirection to malicious sites for phishing or to evade security filters. The attack requires no authentication and works on public-facing endpoints, with impacts including user deception and potential credential theft as per CWE-601.

## Requirements

1. Internet access to the target domains (skyliner.io, qa.skyliner.io)
2. curl or a web browser for testing
3. No special privileges or tools beyond basic HTTP clients

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to enforce absolute schemes (e.g., require http/https) and block protocol-relative redirects
- Use Content Security Policy (CSP) with redirect restrictions
- Monitor server logs for suspicious 301 responses with unusual Location headers
- Employ web application firewalls (WAF) to detect double-slash patterns in URLs

## Objectives

1. Verify the presence of the open redirect vulnerability
2. Demonstrate redirection to an untrusted domain
3. Assess potential for phishing exploitation

## Instructions

### Step 1: Craft and Test Vulnerable URL on Production Domain

**Context**: Construct a URL with double slash to trigger the redirect and use curl to inspect the response headers.

**Command** ([[commands/curl-fetch-url-with-redirect]]):
```bash
curl -I https://skyliner.io//blackfan.ru/
```

> This command sends a HEAD request to the manipulated URL. Expected output includes HTTP/1.1 301 Moved Permanently and Location: //blackfan.ru, confirming the vulnerability without following the redirect.

### Step 2: Repeat Test on QA Domain

**Context**: Validate the issue persists across environments to assess scope.

**Command** ([[commands/curl-fetch-url-with-redirect]]):
```bash
curl -I https://qa.skyliner.io//blackfan.ru/
```

> Similar to Step 1, look for the 301 response with the arbitrary Location header. Success indicates broad exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-url-with-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[web-vulnerability]]
