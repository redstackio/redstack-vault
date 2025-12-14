---
tags:
  - csrf
  - token-leak
  - reconnaissance
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9688e94a-d995-4463-b894-8d79dabb6cbe
created_at: '2025-12-14T17:33:24.529Z'
updated_at: '2025-12-14T17:33:24.529Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover CSRF Token Leak in Public JavaScript File

## Summary

This procedure identifies the exposure of a session-specific CSRF protection token ('rt') in Bumble's publicly accessible JavaScript file, enabling attackers to obtain tokens without authentication for subsequent exploitation.

## Description

In the context of Bumble's social account linking, the 'rt' parameter serves as a CSRF token to validate requests. However, it is inadvertently embedded in the chrome-service-worker.js file under the url_stats variable. An attacker can access this file directly, parse the content, and retrieve the token tied to the victim's session if they inspect it while the victim is authenticated. This leak undermines the CSRF protection, allowing reuse in crafted requests. Prerequisites include a victim's active session; the attacker needs no credentials but must entice the victim to load related resources.

## Requirements

1. Browser access to https://eu1.badoo.com
2. Victim must be logged into Bumble to generate a session-specific 'rt' token
3. Basic web inspection skills (e.g., viewing source or using curl)

## Defense

Defensive measures and detection strategies:

- Remove sensitive tokens from client-side JavaScript files; generate them dynamically server-side
- Implement Content Security Policy (CSP) to restrict script loading from untrusted sources
- Monitor access logs for anomalous requests to service worker files

## Objectives

1. Locate and confirm the 'rt' token exposure in public resources
2. Document the leak format for PoC development
3. Validate token uniqueness per session

## Instructions

### Step 1: Access the Service Worker File

**Context**: Retrieve the JavaScript file containing the leaked token to inspect its contents.

Use a browser or command-line tool to fetch the file:

```bash
curl https://eu1.badoo.com/worker-scope/chrome-service-worker.js
```

> This command downloads the JS file. Search the output for 'url_stats' to find the string like 'https://eu1.badoo.com/chrome-push-stats?ws=1&rt=<rt_value>'. The 'rt' value is the leaked CSRF token.

### Step 2: Parse and Verify Token

**Context**: Confirm the token's presence and format within the file.

Open the downloaded file in a text editor and locate the url_stats variable. Note the 'rt' parameter after '&rt='.

> Expected: A unique string (e.g., a hash) specific to the session. If the victim reloads the page, a new token should appear, confirming session-binding.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-leak]]
- [[Reconnaissance]]
