---
id: p1q2r3s4-t5u6-7890-bcde-fg1234567890
name: Identify-Google-Drive-Integration
tags:
  - recon
  - ssrf
  - google-drive
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inspect-element]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:24.217Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Google-Drive-Integration

## Summary

This procedure involves scouting a web application's user interface and network traffic to identify integrations with Google Drive that could be abused for SSRF, such as file import features that proxy requests server-side.

## Description

In applications like Uber's web platform, Google Drive integration allows users to import files, but the backend fetches the content directly from Google servers. Without proper URL validation, attackers can manipulate URLs to force requests to internal resources. This targets public-facing web apps on cloud platforms like AWS, where metadata services are accessible via localhost or link-local IPs.

## Requirements

1. Access to a valid user session on the target web app
2. Browser with developer tools or proxy like Burp Suite
3. Knowledge of the app's file handling features

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed domains for proxy requests
- Disable direct server-side fetches for third-party integrations
- Monitor for anomalous outbound requests to internal IPs

## Objectives

1. Locate SSRF-prone endpoints
2. Confirm server-side request handling
3. Identify bypass opportunities like IP restrictions

## Instructions

### Step 1: Explore Application Features

**Context**: Search for Google Drive-related functionality, such as 'Import from Drive' buttons.

**Command** ([[commands/inspect-element]]):
```bash
# Use browser dev tools: Right-click element > Inspect > Network tab
```

> Load the import page and trigger a Drive link; observe requests to drive.google.com from the server.

### Step 2: Intercept and Analyze Traffic

**Context**: Use a proxy to capture backend interactions.

**Command** ([[commands/burp-intercept]]):
```bash
# Configure browser proxy to Burp; intercept POST to /api/import
```

> Look for JSON payloads with 'url' fields containing Google Drive links; note lack of IP checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/inspect-element]]
- [[commands/burp-intercept]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[ssrf]]
