---
id: proc-irccloud-get-verify-7357
tags:
  - open-redirect
  - get-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-get-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:26.243Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Verify-Open-Redirect-on-GET-Requests

## Summary

This procedure tests the open redirect vulnerability specifically on GET requests to irccloud.com, confirming it operates independently of CSRF tokens or POST-specific protections, broadening the attack surface.

## Description

GET requests to endpoints like /login on irccloud.com suffer from the same Host header validation flaw. By manipulating the Host header in a GET request, the server redirects to the arbitrary domain without additional checks. This verification step uses screenshots or logs to document the behavior, highlighting that the issue affects standard browsing flows and not just form submissions.

## Requirements

1. Ability to send custom GET requests (e.g., via curl or browser dev tools)
2. Access to irccloud.com
3. Logging or screenshot capability for evidence

## Defense

Defensive measures and detection strategies:

- Enforce CSRF protections on all endpoints, though ineffective here
- Log and alert on GET requests with mismatched Host headers
- Redirect only to whitelisted internal domains

## Objectives

1. Confirm redirect functionality on GET methods
2. Demonstrate no dependency on tokens or POST data
3. Evaluate exploitability in real user scenarios

## Instructions

### Step 1: Send GET Request with Host Manipulation

**Context**: Target a common GET endpoint like /login and inject a malicious Host to trigger the redirect.

**Command** ([[commands/curl-verify-get-redirect]]):
```bash
curl -H "Host: malicious-site.com" -X GET http://irccloud.com/login -v
```

> The command performs a GET to /login with overridden Host. Verbose output reveals a redirect Location header to the malicious site, proving the vulnerability on GET without CSRF involvement.

### Step 2: Document and Validate Independence

**Context**: Review the response to ensure no token validation blocks the redirect, simulating a browser request.

**Command** ([[commands/curl-verify-get-redirect]]):
```bash
curl -H "Host: test-redirect.com" -X GET http://irccloud.com/ -i -L
```

> The -L flag follows the redirect for full trace. Expected output shows navigation to the test domain, confirming clean exploitation on GET requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-get-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[get-request]]
