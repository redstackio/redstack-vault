---
id: proc-1066410-004
tags:
  - poc
  - phishing
  - validation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/test-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:39.489Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate Open Redirect PoC

## Summary

This procedure tests and documents the created short link to prove the open redirect vulnerability, showing how it can lead to malicious sites under a trusted domain.

## Description

After generating a short link, follow it to confirm the redirect chain, simulating user interaction for phishing. Record via screenshot or video. Target: Generated lnk.clario.co link. Prerequisites: Valid short link from prior exploitation. Outcomes: Verified redirect to arbitrary domain.

## Requirements

1. Generated short link from API exploitation
2. Browser or curl for testing
3. Video recording tool for PoC

## Defense

Defensive measures and detection strategies:

- Add redirect confirmation pages or warnings
- Scan short links for suspicious patterns before activation
- User education on verifying short URLs

## Objectives

1. Confirm redirect functionality
2. Document impact for reporting
3. Highlight phishing potential

## Instructions

### Step 1: Follow and Test the Short Link

**Context**: Simulate user click to validate the open redirect.

**Command** ([[commands/test-redirect]]):
```bash
curl -L 'https://lnk.clario.co/abc123' -v
```

> Follows redirects with verbose output. Expected output: 302 to https://evil.com, confirming bypass.

### Step 2: Record PoC

**Context**: Capture the flow for evidence.

Use browser dev tools or screen recording to show the redirect from clario.co to malicious site.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/test-redirect]]

## Tools Used


## Tags

- poc
- phishing
- validation
