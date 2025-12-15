---
tags:
  - intercept
  - modify
  - web
  - http
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:15.997Z'
sub_techniques: []
id: 30174e47-c3c8-48fb-a000-cfc69a9c24e7
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-and-Modify-Request-Parameters

## Summary

This procedure captures and alters HTTP requests to the /affiliates/stats endpoint, demonstrating parameter malleability for CSRF exploitation.

## Description

Using browser tools, intercept the POST or GET request when submitting stats filters, then edit parameters like start_date or end_date to arbitrary values. This confirms the lack of validation, enabling forged CSRF attacks.

## Requirements

1. Developer tools enabled in browser
2. Stats page loaded
3. Knowledge of HTTP request structure

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing requests
- Validate parameter ranges server-side

## Objectives

1. Capture baseline request
2. Successfully modify and resubmit
3. Observe endpoint acceptance

## Instructions

### Step 1: Enable Interception

**Context**: Set up request monitoring.

Open browser developer tools (F12), go to the Network tab, and filter for the stats endpoint.

### Step 2: Trigger and Intercept

**Context**: Capture the request.

Submit a stats query on the page; right-click the request in the Network tab and select 'Copy as cURL' or edit directly.

### Step 3: Modify and Replay

**Context**: Alter parameters.

Edit fields like date ranges (e.g., change to '2023-01-01' to '2023-12-31'), then replay the request via the tools or console.

> The page updates with the new stats, indicating no protection against modifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- intercept
- web
