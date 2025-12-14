---
tags:
  - redirect-bypass
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T04:38:49.202Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: f610d38e-6cc3-463e-98e1-59909c7c70aa
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Attempt-Open-Redirect-Bypass

## Summary

This procedure tests for open redirect vulnerabilities in Shopify's login flow, aiming to chain redirects with domain takeovers, though it fails due to existing filters.

## Description

Using black box interception, modify login redirect parameters to external domains. This explores chaining vectors but highlights robust filtering, pivoting attackers to logic flaws.

## Requirements

1. Active trial account
2. Burp Suite proxy setup
3. Knowledge of HTTP parameter tampering

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against allowlist
- Log anomalous redirect attempts
- Use Content Security Policy

## Objectives

1. Identify redirect weaknesses
2. Chain with domain exploits if successful
3. Confirm filter efficacy

## Instructions

### Step 1: Intercept Login Request

**Context**: Capture the login flow to modify redirect.

Configure [[tools/Burp-Suite]] as proxy and navigate to login.

> Expected: Request visible in Burp Repeater.

### Step 2: Modify and Submit

**Context**: Tamper with redirect parameter.

In Burp, change `redirect` to `//acme` and forward.

**Command** (no CLI, browser via proxy):

> Expected: Blocked by filter, no redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[redirect-bypass]]
- [[web]]
