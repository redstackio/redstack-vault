---
id: proc-observe-redirect-dos-52035
tags:
  - dos
  - open-redirect
  - cloudflare
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:24:30.670Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Observe Open Redirect and DoS Effect

## Summary

This procedure verifies the success of the open redirect and demonstrates a secondary DoS impact from CloudFlare's handling of double-slash URLs, which can temporarily disrupt access.

## Description

Upon triggering the redirect, the browser navigates to the external domain, confirming the phishing potential. Additionally, direct access to double-slash paths like `https://hackerone.com//anything/hacktivity` elicits a CloudFlare 523 error (origin unreachable), and this error state may cache briefly, affecting subsequent requests to clean URLs.

## Requirements

1. Successful redirect from prior procedure
2. Web browser developer tools for inspection
3. Multiple test URLs for DoS verification

## Defense

Defensive measures and detection strategies:

- Configure CloudFlare or similar CDNs to properly handle malformed URLs without error propagation.
- Implement client-side validation to prevent navigation to suspicious URLs.
- Monitor for high volumes of 523 errors or redirect patterns in logs to detect abuse.

## Objectives

1. Confirm the redirect leads to the intended external site.
2. Trigger and observe the DoS error on malformed paths.
3. Note any persistence of the error state for impact assessment.

## Instructions

### Step 1: Verify the Redirect

**Context**: Check the final destination after language switch to ensure external domain access.

Observe the browser's navigation post-switch.

> Expected: Lands on `http://example.com/` or similar, with no HackerOne content.

### Step 2: Test DoS on Double-Slash URL

**Context**: Access a non-existent path with double slashes to invoke CloudFlare error.

Navigate to `https://hackerone.com//anything/hacktivity`.

> Expected: CloudFlare error 523 displayed; test a clean URL immediately after to check for temporary DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- cloudflare-error
- redirect-observation
