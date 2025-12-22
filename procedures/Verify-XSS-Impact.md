---
tags:
  - impact-verification
  - session-theft
  - acronis
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-13T23:56:03.481Z'
sub_techniques: []
id: 6ae848ba-0c5f-46d7-bf93-708a7410c511
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Unsecured Credentials]]'
---
# Verify XSS Impact

## Summary

This procedure assesses the consequences of the stored XSS, such as potential session cookie theft or unauthorized actions, confirming the vulnerability's severity.

## Description

Post-execution, evaluate by replacing the prompt with code to access document.cookie or perform clicks. In the victim context, this enables phishing or account takeover. Requires successful trigger; outcomes highlight risks like data exfiltration.

## Requirements

1. Executed XSS payload
2. Developer tools for inspection
3. Knowledge of advanced payloads

## Defense

Defensive measures and detection strategies:

- HttpOnly and Secure flags on cookies
- Monitor for unauthorized API calls from sessions
- Regular XSS scanning in CI/CD

## Objectives

1. Demonstrate JavaScript context execution
2. Simulate real impacts like theft
3. Report vulnerability details

## Instructions

### Step 1: Inspect Execution

**Context**: Use browser dev tools to monitor effects.

Open console during trigger; observe prompt and domain.

> Confirms execution in site context.

### Step 2: Test Advanced Payload

**Context**: Modify for impact simulation.

Replace prompt with `document.cookie` alert or fetch to external server.

> Alerts show cookies; potential exfil path.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- impact-assessment
- data-exfiltration
