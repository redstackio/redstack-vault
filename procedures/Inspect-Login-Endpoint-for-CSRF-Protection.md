---
id: proc-uuid-7936-inspect
tags:
  - csrf
  - inspection
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-login-inspect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:23.480Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Login-Endpoint-for-CSRF-Protection

## Summary

This procedure involves examining the login form and HTTP requests of a web application to detect the absence of CSRF protection, specifically for JSON-based POST endpoints like Secret.ly's /_/login.

## Description

In the context of Secret.ly, the login endpoint at https://www.secret.ly/_/login uses a JSON payload with 'Login' and 'Password' fields but lacks any CSRF token validation. This allows forged requests from external sites. The procedure uses browser tools or proxies to capture and analyze requests, confirming the vulnerability by attempting token-less submissions. Prerequisites include access to the target site and basic web debugging knowledge. Expected outcomes include identification of the vulnerable endpoint structure for further exploitation.

## Requirements

1. Network access to https://www.secret.ly
2. Browser with developer tools or [[tools/Burp-Suite]]
3. No authentication required for inspection

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Use SameSite cookies to mitigate cross-site requests
- Monitor for anomalous login patterns from unusual referers

## Objectives

1. Confirm absence of CSRF protection
2. Document request payload and headers
3. Identify potential for forged requests

## Instructions

### Step 1: Capture Login Request

**Context**: Use developer tools to intercept the legitimate login attempt and note the absence of tokens.

**Command** ([[commands/curl-login-inspect]]):
```bash
curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -d '{"Login":"test@example.com","Password":"testpass"}'
```

> This command sends a sample JSON request. Expected output is a response without CSRF errors, confirming the vulnerability.

### Step 2: Analyze Response

**Context**: Review headers and body for any validation mentions.

No specific command; manually inspect using Burp or browser console.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-login-inspect]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web-inspection]]
