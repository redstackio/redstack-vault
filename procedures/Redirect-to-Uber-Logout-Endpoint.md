---
tags:
  - logout
  - redirect
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 35eb0acc-c9a4-4e02-b4da-37092e2891b2
created_at: '2025-12-11T06:10:15.763Z'
updated_at: '2025-12-11T06:10:15.763Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0008]]'
mitre_techniques:
  - '[[T1550]]'
---
# Redirect to Uber Logout Endpoint

## Summary

This procedure processes the redirect to Uber's logout endpoint, setting up the final Referer-based redirection for token leakage.

## Description

The auth.uber.com redirects to login.uber.com/logout based on next_url. This endpoint is vulnerable to Referer header manipulation, allowing external redirects with sensitive data.

## Requirements

1. Successful chaining from prior redirect
2. Control over HTTP headers in the request chain
3. Victim's session context

## Defense

Defensive measures and detection strategies:

- Avoid using Referer for redirection logic
- Sanitize and validate all redirect targets

## Objectives

1. Reach the logout endpoint
2. Trigger the vulnerable redirection behavior
3. Position for token exfiltration

## Instructions

### Step 1: Handle Next URL Redirect

**Context**: auth.uber.com redirects to logout.

The redirect URL is:

```
https://login.uber.com/logout
```

> This is automatic; ensure Referer is set to attacker site in the request.

### Step 2: Prepare for Referer Check

**Context**: Set up headers for the next step.

Use browser or proxy to ensure Referer: https://attacker.com.

> Proceed to token leak upon redirection.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[logout]]
- [[redirect]]
