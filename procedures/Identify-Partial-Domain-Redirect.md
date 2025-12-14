---
id: proc-identify-partial-domain-redirect
tags:
  - partial-redirect
  - domain-truncation
  - phishing
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.327Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Partial Domain Redirect

## Summary

This procedure exploits a URL parsing flaw causing partial domain truncation in redirects on hackerone.com, where encoded domains like %2Fgoogle.com redirect to incomplete URLs like https://google, revealing exploitable inconsistencies.

## Description

The server's handling of encoded slashes leads to cutting off domain suffixes (e.g., .com), resulting in partial redirects. Tested in a web browser on hackerone.com, this requires no special access and demonstrates a stepping stone to full redirects, with phishing potential via misleading destinations.

## Requirements

1. Browser for URL access
2. Connectivity to partial external domains
3. hackerone.com availability

## Defense

Defensive measures and detection strategies:

- Validate full domain structure in redirect logic
- Reject redirects with incomplete or malformed domains
- Use regex to detect truncation patterns in logs

## Objectives

1. Expose domain truncation in redirect parsing
2. Confirm partial redirect feasibility
3. Pave way for encoding bypasses

## Instructions

### Step 1: Access Encoded Domain URL

**Context**: Use a single-encoded domain after %2F to trigger truncation.

Navigate to: `https://hackerone.com/%2Fgoogle.com`

> Server parses %2F as path separator but truncates .com, redirecting to https://google. Expected output: Incomplete redirect to base domain.

### Step 2: Validate Truncation Effect

**Context**: Confirm the redirect destination lacks the full domain.

Check browser address bar post-redirect.

> Success shows redirect to https://google, not google.com, indicating parsing bug.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- partial-redirect
- domain-truncation
