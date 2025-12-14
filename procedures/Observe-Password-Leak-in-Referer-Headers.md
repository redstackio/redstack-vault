---
tags:
  - observation
  - leak
  - referer
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - macOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:10.195Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8df6fc70-c4ca-4b93-8dac-a4b6fa3b0042
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Unsecured Credentials]]'
---
# Observe-Password-Leak-in-Referer-Headers

## Summary

This procedure involves monitoring proxied traffic in Burp Suite to detect and document the exposure of the Core API Password in Referer headers sent to third-party domains during Blockstack Browser interactions.

## Description

Upon accessing the sign-up page, the Blockstack app makes requests to external services like appco.imgix.net, api.app.co, and browser-api.blockstack.org. These requests include URLs with the Core API Password as a query parameter, which is then copied into the Referer header. Without a Referer-Policy, this leaks the password in plaintext, potentially to logs or compromised endpoints. The outcome is evidence of the vulnerability for reporting.

## Requirements

1. Active Burp Suite proxy intercepting traffic
2. Blockstack app running and sign-up accessed
3. Knowledge of HTTP headers and query parameters

## Defense

Defensive measures and detection strategies:

- Set Referer-Policy: no-referrer or strict-origin-when-cross-origin
- Avoid sensitive data in URLs; use POST bodies instead
- Audit third-party requests and log Referer headers for anomalies

## Objectives

1. Capture requests to identified third-party domains
2. Extract and verify password in Referer header
3. Assess impact on user credential security

## Instructions

### Step 1: Monitor Proxy Traffic

**Context**: Switch to Burp's Proxy > HTTP history tab to view intercepted requests.

No command required; inspect in UI.

> Filter for requests from localhost:8888 and look for outbound connections post-sign-up access.

### Step 2: Inspect Referer Headers

**Context**: Examine headers for URLs containing the Core API Password parameter.

No command required; right-click request and view details.

> Note Referer headers in requests to appco.imgix.net, api.app.co, browser-api.blockstack.org; confirm password like ?coreApiPassword=example123 is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System
- [[Unsecured Credentials]] Unprotected Storage of Credentials

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- traffic-analysis
- credential-leak
- http-headers
