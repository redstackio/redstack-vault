---
id: proc-uuid-002
name: Identify-SQL-Injection-Points
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.449Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - recon
  - sqli
  - web
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Identify-SQL-Injection-Points

## Summary

This reconnaissance procedure scans a web application to identify parameters vulnerable to SQL Injection by testing for error responses or behavioral changes indicative of unsanitized inputs.

## Description

In the Palantir files service scenario (CVE-2021-38159), this involves inspecting network requests to https://files.palantir.com/ for input fields like query strings or form data. Manual testing with payloads reveals injection points. This step is crucial before exploitation to map the attack surface without triggering alerts.

## Requirements

1. Access to a web proxy or browser dev tools
2. Knowledge of common SQL error patterns
3. Target URL: https://files.palantir.com/

## Defense

Defensive measures and detection strategies:

- Log all input validation failures
- Rate-limit suspicious requests
- Employ input sanitization at the application layer

## Objectives

1. Locate injectable parameters
2. Confirm vulnerability type (error-based, blind, etc.)
3. Minimize footprint during testing

## Instructions

### Step 1: Inspect Application Requests

**Context**: Use a proxy to capture and analyze traffic to the target endpoint.

Intercept requests to https://files.palantir.com/ and identify parameters (e.g., 'file=1').

### Step 2: Basic Injection Test

**Context**: Append payloads to parameters and observe responses.

Test with ' or " to provoke errors. Look for messages like "You have an error in your SQL syntax".

### Step 3: Validate with Time-Based or Boolean Tests

**Context**: For blind SQLi, use SLEEP() or conditional statements.

Example payload: file=1 AND SLEEP(5). Delay in response confirms blind injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[sqli]]
