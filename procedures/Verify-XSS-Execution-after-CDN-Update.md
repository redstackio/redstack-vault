---
tags:
  - xss
  - verification
  - cdn
  - devtools
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
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
updated_at: '2025-12-13T23:55:20.697Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 72c7ffe2-d6a2-430d-9cd2-5efb45ec51c3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-Execution-after-CDN-Update

## Summary

This procedure monitors CDN cache updates after malicious graphie upload and verifies XSS payload execution using browser tools, confirming DOM injection on Khan Academy pages.

## Description

After upload, the malicious graphie propagates to CDNs like cdn.kastatic.org and S3. Rendering triggers the payload via onload or script insertion. Use DevTools to simulate or wait for real propagation and inspect execution.

## Requirements

1. Access to a browser and the affected Khan Academy page rendering the target graphie
2. Uploaded malicious graphie hash/URL from prior step
3. Patience for cache TTL (may take minutes)

## Defense

Defensive measures and detection strategies:

- Implement cache invalidation on suspicious uploads
- Log and alert on graphie renders with anomalous content
- Browser-side: Enforce strict CSP and sanitize DOM insertions
- Monitor for unexpected JS execution in graphie contexts

## Objectives

1. Confirm cache update with malicious content
2. Trigger and observe XSS payload
3. Validate impact on account takeover potential

## Instructions

### Step 1: Monitor CDN Propagation

**Context**: Wait or poll for the malicious graphie to appear in CDN responses.

Use browser to load the Khan Academy page with the graphie. Check Network tab in DevTools for requests to cdn.kastatic.org or ka-perseus-graphie.s3.amazonaws.com.

> Expected: Response contains malicious SVG/JSON after cache update.

### Step 2: Simulate and Verify Execution

**Context**: Override network response in DevTools to test payload immediately, or wait for natural load.

In DevTools Network tab, right-click the graphie JSON/SVG request > "Override content" > Paste malicious JSON/SVG. Refresh page.

Inspect Console for errors and Elements for injected script/onload.

> Expected: Alert or console output from payload (e.g., alert('XSS')). Success if JS executes in DOM.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- xss
- verification
- cdn
