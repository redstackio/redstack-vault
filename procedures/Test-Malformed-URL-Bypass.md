---
id: proc-test-malformed-bypass
tags:
  - open-redirect
  - url-bypass
  - malformed-url
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:23.515Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Test-Malformed-URL-Bypass

## Summary

This procedure exploits insufficient validation in the 'continue' parameter by using a malformed URL with a single slash ('http:/'), bypassing restrictions and enabling redirection to external sites for potential phishing.

## Description

The vulnerability arises from the application's failure to normalize or properly parse URLs with missing slashes after the protocol. By crafting 'http:/example.com' instead of 'http://example.com', the redirect validation skips external domain checks, allowing attackers to lure users to malicious sites after login. This was discovered through manual URL manipulation testing.

## Requirements

1. Internet access to khanacademy.org
2. Web browser or curl tool
3. Knowledge of target external domain for testing

## Defense

Defensive measures and detection strategies:

- Normalize all URLs before validation (e.g., add missing slashes)
- Use regex to detect and block malformed protocols
- Implement redirect logging with WAF rules for suspicious patterns

## Objectives

1. Bypass URL validation using malformed protocol
2. Achieve arbitrary external redirect
3. Facilitate phishing by mimicking legitimate post-login navigation

## Instructions

### Step 1: Access Login with Malformed URL

**Context**: Send a request to the login page with a 'continue' parameter using 'http:/' to trigger the bypass.

**Command** ([[commands/curl-access-url]]):
```bash
curl -L "https://www.khanacademy.org/login?continue=http:/www.olivierbeg.nl"
```

> This follows redirects and accesses the malformed URL. Expected output is a successful HTTP redirect (301/302) to the external site, confirming the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[open-redirect]]
- [[url-bypass]]
