---
id: uuid-identify-bypass
tags:
  - ssrf
  - bypass
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.745Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-SSRF-Bypass-Opportunities

## Summary

This procedure tests the readapi variable's restrictions to find bypasses, such as redirect following to HTTP/internal endpoints, enabling SSRF exploitation.

## Description

By probing limitations like HTTPS enforcement, content-type checks, and timeouts, attackers can confirm redirect-based bypasses to internal services like AWS metadata. This applies to Streamlabs Cloudbot, with outcomes including error messages for invalid requests and success for redirects.

## Requirements

1. Streamlabs chat access for testing commands
2. Test URLs (HTTPS and HTTP)
3. Knowledge of HTTP redirects and AWS metadata service

## Defense

Defensive measures and detection strategies:

- Disable redirect following in backend HTTP client
- Validate full URL path post-redirect to block internal IPs
- Monitor for frequent error responses like [Https required]

## Objectives

1. Confirm HTTPS-only but redirect-following behavior
2. Document limitations (content-type, timeout, etc.)
3. Prepare for redirect-based SSRF

## Instructions

### Step 1: Test HTTPS Enforcement

**Context**: Verify non-HTTPS URLs are blocked.

Use {readapi.http://example.com} in chat command.

> Expected: [Https required] error.

### Step 2: Test Redirect to HTTP

**Context**: Check if backend follows redirects.

Host a test redirect to HTTP and use {readapi.https://redirect-to-http} in command.

> Expected: Successful fetch of HTTP content via redirect.

### Step 3: Note Limitations

**Context**: Identify response constraints.

Test non-2xx, invalid content-type, or long responses.

> Expected: Errors like [Bad Server Response / Too slow] or [Invalid Content-Type].

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[bypass]]
