---
tags:
  - cors
  - recon
  - misconfiguration
type: procedure
tools:
  - '[[tools/Browser-Firefox]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/test-cors-with-custom-origin]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:12.116Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 18ca51b0-ecfe-4fef-9f0f-ccd3bed37f03
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Test-CORS-Policy-with-Custom-Origin

## Summary

This procedure tests for CORS misconfigurations by sending requests with arbitrary Origin headers to observe if the server echoes them in Access-Control-Allow-Origin without validation, enabling potential cross-origin attacks.

## Description

In the context of nordvpn.com's WordPress REST API, the server sets Access-Control-Allow-Origin to the client's Origin header dynamically and includes Access-Control-Allow-Credentials: true. This allows any site to make authenticated requests on behalf of users. The procedure involves crafting a GET request to /wp-json/ and inspecting response headers. Prerequisites include network access to the target and tools like curl or a browser.

## Requirements

1. Network access to https://nordvpn.com
2. Curl or browser developer tools
3. Basic understanding of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement a strict whitelist for allowed origins in CORS policy
- Avoid dynamically echoing Origin; use null or specific values
- Monitor for unusual Origin headers in server logs
- Use Content-Security-Policy to restrict cross-origin fetches

## Objectives

1. Confirm if arbitrary origins are permitted with credentials
2. Identify vulnerable endpoints like WordPress REST API
3. Gather evidence for reporting or exploitation planning

## Instructions

### Step 1: Send Test Request

**Context**: Craft and send a GET request to the target endpoint with a custom Origin to probe the CORS policy.

**Command** ([[commands/test-cors-with-custom-origin]]):
```bash
curl -X GET https://nordvpn.com/wp-json/ -H "Origin: http://iamsoevil.com/" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0" -v
```

> This command sends a GET to /wp-json/ with a fake Origin. Expected output includes verbose (-v) headers showing Access-Control-Allow-Origin: http://iamsoevil.com/ and Access-Control-Allow-Credentials: true, confirming the misconfiguration.

### Step 2: Validate Response

**Context**: Inspect the response to ensure the Origin is reflected insecurely.

**Command** (Manual inspection):
```bash
# No command; use curl output or browser network tab
```

> Check for the echoed Origin and credentials flag. If present, the endpoint is vulnerable to cross-origin attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/test-cors-with-custom-origin]]

## Tools Used

- [[tools/Browser-Firefox]]

## Tags

- cors
- recon
- web
