---
id: proc-004
tags:
  - xss-execution
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-alert-and-log-sensitive-data]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:18.423Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Admin-Panel

## Summary

With an admin tab open, the postMessage triggers handleRoutePushEvent to load the XSS page into the admin frame, executing the payload in high-privilege context.

## Description

The vulnerability in Shopify.API.pushState allows '..' traversal to escape /admin, loading /pages/xss into AppFrameMain. This executes the XSS, stealing data like CSRF tokens.

## Requirements

1. Open admin tab (e.g., themes)
2. Trigger page activated
3. XSS page exists

## Defense

- Validate pathname against /admin prefix
- Allowlist valid routes
- Frame isolation policies

## Objectives

1. Load arbitrary page in admin
2. Execute XSS for data collection
3. Confirm privilege escalation

## Instructions

### Step 1: Prepare Admin Tab

**Context**: Open admin to a section like themes.

**Instructions**: Navigate to /admin/themes in existing tab.

> Expected output: Admin interface loaded.

### Step 2: Trigger and Observe

**Context**: postMessage loads the payload.

**Instructions**: From trigger page, ensure messages send; switch to admin tab.

> XSS from [[commands/xss-alert-and-log-sensitive-data]] executes. Expected output: Alert and console logs with cookies, token.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-alert-and-log-sensitive-data]]

## Tools Used

- [[tools/Google-Chrome]]

## Tags

- xss-execution
