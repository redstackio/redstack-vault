---
id: proc-wordpress-construct-url-001
tags:
  - oauth
  - url-construction
  - reflection
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:37.247Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Construct-OAuth-Authorize-URL

## Summary

This procedure builds a victim-facing OAuth authorize URL using the client ID from the malicious app, setting up reflection of the stored XSS payload.

## Description

Using the client ID obtained from app creation, this step assembles the OAuth2 authorize endpoint URL with parameters for redirect and response type. The target is https://public-api.wordpress.com/oauth2/authorize, where the app description is reflected unsanitized. This enables any user visiting the URL to view the injected content in their session context.

## Requirements

1. Client ID from payload injection step
2. Template URL knowledge
3. Browser for URL access

## Defense

Defensive measures and detection strategies:

- Escape reflected app metadata in OAuth pages
- Validate client_id parameters against known apps
- Log and alert on suspicious OAuth requests

## Objectives

1. Create accessible URL for payload reflection
2. Ensure parameters match app redirect
3. Prepare for victim interaction

## Instructions

### Step 1: Build and Access URL

**Context**: Substitute variables to form the full authorize endpoint.

No command required; replace YOUR_CLIENT_ID in `https://public-api.wordpress.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=https://google.com&response_type=code&blog=` with the actual ID (e.g., 123456), then open in a browser.

> Expected output: OAuth page loads, showing app details including the injected description with HTML elements visible in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[wordpress]]
