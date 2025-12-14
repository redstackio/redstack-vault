---
id: proc-uber-oauth-url-craft
tags:
  - xss
  - oauth
  - url-crafting
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
updated_at: '2025-12-14T17:24:35.193Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-OAuth-URL-for-XSS

## Summary

This procedure constructs a malicious OAuth authorization URL for Uber's endpoint by embedding a javascript: URI in the redirect_uri parameter, exploiting weak protocol validation to set up XSS payload delivery.

## Description

The Uber OAuth /authorize endpoint validates redirect_uri only for the presence of '://' but fails to restrict protocols, allowing javascript: URIs. This enables arbitrary JS execution upon redirect in vulnerable browsers. The procedure involves selecting a client_id, setting response_type=code, scope=profile, and encoding a JS payload like alert(document.domain) in the redirect_uri. Prerequisites include knowledge of a valid client_id from Uber's app registry or testing.

## Requirements

1. Valid client_id from Uber OAuth apps (e.g., MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS)
2. URL encoding tool for payloads (e.g., %0A for newline in JS)
3. Access to a vulnerable browser for testing

## Defense

Defensive measures and detection strategies:

- Strictly validate and whitelist allowed protocols and domains in redirect_uri (e.g., only https://*.uber.com)
- Use Content-Security-Policy (CSP) to block inline JS execution
- Monitor for anomalous redirect_uri patterns in logs, such as javascript: or data:
- Disable or sanitize Location header redirects in OAuth responses

## Objectives

1. Create a functional malicious URL that passes initial validation
2. Encode JS payload to execute on redirect
3. Prepare for distribution to target users

## Instructions

### Step 1: Select Parameters and Encode Payload

**Context**: Gather OAuth parameters and encode the JS payload to evade basic filters.

Construct the base URL with client_id, response_type, and scope. Set redirect_uri to 'javascript://example.com/%0Aalert(document.domain);//' and URL-encode it (%2F%2F for //, %250A for \n, etc.).

Example full URL:

```url
https://login.uber.com/oauth/authorize?client_id=MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS&response_type=code&scope=profile&redirect_uri=javascript%3A%2F%2Fgoog.com%2F%250Aalert%28document.domain%29%3B%2F%2F
```

> This URL, when visited, presents the consent page with the malicious redirect prepared.

### Step 2: Validate URL Construction

**Context**: Test the URL in a browser to ensure it loads the OAuth page without errors.

Paste the URL into a vulnerable browser's address bar and confirm the Uber login/consent page appears.

> Expected: Page loads; no 400/redirect errors. Payload remains intact for later execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[oauth]]
- [[url-crafting]]
