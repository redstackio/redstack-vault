---
id: proc-uuid-1
tags:
  - ssrf
  - url-redirection
  - bypass
type: procedure
tools:
  - '[[tools/TinyURL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:18.677Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Redirect-URL-to-Internal-Endpoint-Using-TinyURL

## Summary

This procedure creates a URL shortening via TinyURL that redirects to an internal endpoint like http://0:6000/, evading SSRF filters that only validate the initial URL without following redirects.

## Description

In the context of exploiting blind SSRF in web APIs like Infogram's, attackers craft external URLs that redirect to localhost or internal IPs. This targets environments where direct internal URLs are blocked, but external services are permitted. Prerequisites include access to a URL shortener and knowledge of target internal ports. Expected outcome is a benign-looking URL that triggers internal fetches.

## Requirements

1. Internet access to TinyURL service
2. Knowledge of target internal port (e.g., 6000)
3. No special credentials needed

## Defense

Defensive measures and detection strategies:

- Implement redirect-following in URL validation filters
- Block or monitor requests to known URL shorteners
- Use web application firewalls (WAF) to detect anomalous redirects

## Objectives

1. Generate an external URL proxying to internal resources
2. Verify redirect functionality
3. Prepare payload for SSRF trigger

## Instructions

### Step 1: Generate TinyURL Redirect

**Context**: Access TinyURL and create a custom alias redirecting to the internal endpoint.

**Command** ([[commands/curl-verify-redirect]]):
```bash
curl -I "https://tinyurl.com/ybk7sqrg"
```

> This command performs a HEAD request to verify the redirect resolves to http://0:6000/. Expected output includes Location header pointing to the internal URL.

### Step 2: Test Redirect Resolution

**Context**: Confirm the short URL behaves as intended without direct access to internals.

No specific command; manually access the TinyURL in a browser or use curl to observe the 3xx redirect status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-redirect]]

## Tools Used

- [[tools/TinyURL]]

## Tags

- ssrf
- redirection
