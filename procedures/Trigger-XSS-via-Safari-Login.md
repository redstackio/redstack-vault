---
id: uuid-4
tags:
  - trigger
  - xss
  - safari
  - login
type: procedure
tools:
  - '[[tools/Safari]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.334Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Safari-Login

## Summary

This procedure initiates the Nextcloud login flow in Safari to trigger the stored XSS from the malicious authorization_endpoint, exploiting the unencoded meta refresh workaround.

## Description

Safari's user agent detection in user_oidc's LoginController.php causes a meta refresh redirect using the stored endpoint without escaping, injecting the payload into HTML like <meta http-equiv="refresh" content="0; url='" http-equiv=><svg/onload=alert(document.domain)>?client_id=..." />. CSP limits to basic alerts.

## Requirements

1. Configured malicious OIDC provider
2. Safari browser
3. Access to Nextcloud login page

## Defense

Defensive measures and detection strategies:

- Encode all dynamic content in HTML responses
- Strengthen CSP to block inline SVG/onload
- Browser-specific workarounds should use safe redirects (e.g., JS or server-side)

## Objectives

1. Detect Safari and apply vulnerable redirect
2. Execute injected JavaScript
3. Demonstrate payload impact

## Instructions

### Step 1: Open Safari and Navigate to Login

**Context**: Use Safari to trigger user agent detection.

**Instructions**: Launch Safari, go to http://localhost:8081/login.

> Expected: Login page loads, detects Safari.

### Step 2: Initiate OIDC Login

**Context**: Select the malicious provider to fetch and reflect the endpoint.

**Instructions**: Click login with the configured OIDC provider. Inspect the redirect response in dev tools.

> Expected output: Meta tag with injected payload; alert(document.domain) executes, but CSP blocks further JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari]]

## Tags

- trigger
- xss
- safari
- login
