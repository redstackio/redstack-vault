---
id: proc-periscope-oauth-capture-url
tags:
  - oauth
  - redirect-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/oauth-redirect-response]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.237Z'
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
# Capture-OAuth-Redirect-URL

## Summary

This procedure captures the Twitter OAuth authenticate URL from the poisoned response, which includes the temporary OAuth token for later use in victim authorization.

## Description

After poisoning the Host header, the Periscope server responds with an HTML page containing a meta refresh tag redirecting to Twitter's OAuth endpoint. The attacker intercepts this without following the redirect to extract the URL. This step relies on the previous poisoning and uses a proxy to view the response body.

## Requirements

1. Successful poisoned request from prior step
2. Proxy configured to view response bodies
3. Text editor or script to parse the meta tag

## Defense

Defensive measures and detection strategies:

- Implement Content-Security-Policy (CSP) to restrict redirects
- Log all OAuth-related responses and alert on unusual meta refreshes
- Use HTTPS and validate redirect origins

## Objectives

1. Intercept the response from poisoned request
2. Extract the full OAuth authenticate URL
3. Store the oauth_token for phishing

## Instructions

### Step 1: Intercept Poisoned Response

**Context**: View the HTML response after sending the poisoned Host request.

**Command** ([[commands/oauth-redirect-response]]):
```html
<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;https://twitter.com/oauth/authenticate?oauth_token=████████"></head></html>
```

> Parse the meta refresh content attribute to get the URL; expected output is the captured Twitter OAuth link with token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/oauth-redirect-response]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- oauth
- redirect-capture
