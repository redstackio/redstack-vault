---
id: proc-test-protocol-relative-bypass
tags:
  - open-redirect
  - url-bypass
  - protocol-relative
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
updated_at: '2025-12-14T17:24:23.512Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Test-Protocol-Relative-URL-Bypass

## Summary

This procedure demonstrates bypassing an updated open redirect validation in Khan Academy's login by using protocol-relative URLs ('//example.com'), which inherit the current protocol and evade domain checks for external redirects.

## Description

After an initial fix for malformed URLs, the application still failed to handle protocol-relative schemes properly. These URLs ('//') resolve to 'https://' or 'http://' based on the current page, but the validation logic did not parse them as external, allowing redirects to arbitrary sites. This enables phishing by tricking users into external domains post-login.

## Requirements

1. Internet access to khanacademy.org (post-initial fix)
2. Web browser or curl tool
3. Target external domain (e.g., google.be for testing)

## Defense

Defensive measures and detection strategies:

- Explicitly parse and validate protocol-relative URLs as external
- Whitelist only absolute URLs with trusted protocols and domains
- Deploy client-side checks and server-side logging for '//' patterns

## Objectives

1. Exploit protocol-relative URL to bypass validation
2. Confirm persistent redirect vulnerability
3. Enable phishing vectors despite patches

## Instructions

### Step 1: Access Login with Protocol-Relative URL

**Context**: Send a request to the login page with a 'continue' parameter using '//' to bypass updated checks.

**Command** ([[commands/curl-access-url]]):
```bash
curl -L "https://www.khanacademy.org/login?continue=//google.be"
```

> This follows redirects and tests the protocol-relative URL. Expected output is a redirect to https://google.be, indicating successful bypass.

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
- [[protocol-relative]]
