---
tags:
  - csrf
  - token-leakage
  - browser-history
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:27:29.219Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5cf2dc88-0620-4222-ad04-835c19a5525c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Retrieve Leaked CSRF Token from Browser History

## Summary

This procedure involves inspecting the victim's browser history to extract the exposed CSRF token leaked via the verification error redirect, enabling its reuse in attacks.

## Description

Due to the GET method used in the error redirect, the CSRF token is embedded in the URL and persisted in the browser's history. An attacker with access to the victim's browser (e.g., via shared device, malware, or physical access) can retrieve it. The token does not expire on first use, making it valuable for multiple CSRF attempts. This step assumes the leakage from the prior procedure has occurred.

## Requirements

1. Access to the victim's browser history (e.g., same session or device)
2. Prior execution of verification failure to generate the history entry
3. Basic knowledge of browser interfaces

## Defense

Defensive measures and detection strategies:

- Clear browser history regularly or use private browsing
- Disable history logging for sensitive sites
- Detect anomalous history access via endpoint monitoring

## Objectives

1. Locate the leaked token in browser history
2. Extract the token value without alerting the user
3. Validate token reusability

## Instructions

### Step 1: Access Browser History

**Context**: Open the browser's history feature to find the verification URL.

In Chrome, press Ctrl+H (or Cmd+H on Mac) to open history. Search for "robocoin.com/verify" to locate the entry from the failed verification.

> The entry will show the full URL, including ?_csrf=token.

### Step 2: Extract and Copy Token

**Context**: Isolate the token for later use.

Click the history entry or copy the URL from the list. Parse the query parameter to get the token value (e.g., everything after _csrf=).

> Expected: Token string like abc123def456, ready for inclusion in forged requests. Test by noting no immediate invalidation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-leakage]]
- [[browser-history]]
