---
tags:
  - csrf
  - cross-origin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.882Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f53d0385-e415-4a0d-b008-f267807b3681
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-CSRF-Request-on-Page-Load

## Summary

This procedure executes the CSRF request by loading the malicious page in the victim's browser, sending a cross-origin GET to Nextcloud's vulnerable endpoint.

## Description

Upon page load, the browser automatically issues the request using the victim's cookies for authentication. The endpoint /nextcloud/index.php/core/apps/recommended lacks token validation, processing the installation without confirmation.

## Requirements

1. Victim loads the page with active Nextcloud session
2. Same-origin policy allows cross-origin GET (no preflight for simple requests)
3. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens for all non-GET state changes
- Implement SameSite cookies to block cross-site requests
- WAF rules to detect anomalous GETs to admin endpoints

## Objectives

1. Send authenticated request to vulnerable endpoint
2. Initiate app installation process
3. Avoid browser blocks or user notices

## Instructions

### Step 1: Load Page in Victim Browser

**Context**: The victim visits the URL, triggering the embedded request.

No command; browser action:

The img src attribute causes:

GET /nextcloud/index.php/core/apps/recommended HTTP/1.1
Host: target-nextcloud.com
Cookie: nextcloud_session=admin_token

> Expected output: Server receives request, no token check fails.

### Step 2: Confirm Request Transmission

**Context**: Use browser dev tools or proxy to verify.

Intercept with tools like Burp to see request details.

> Expected output: 200 OK response from endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
